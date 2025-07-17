# wifi_scanner.py - Final, a more reliable version

# The main firmware provides these functions and modules to the script's environment.
# We import them here to make the script self-documenting.
import network
import ujson
import time
import ubinascii

# This is a special function provided by the firmware to send data back to the app.
# We assume it exists in the global scope when this script is executed.
# def send_log(message):
#     pass

send_log("--- Wi-Fi Scanner Tool Initialized ---")

def run_scan():
    """Activates the interface, scans for networks, and sends results back."""
    
    sta_if = network.WLAN(network.STA_IF)
    
    # Ensure the interface is active before doing anything
    if not sta_if.active():
        sta_if.active(True)
        # Give the radio a moment to activate
        time.sleep(0.5)

    if not sta_if.isconnected():
        send_log("Error: Wi-Fi is disconnected. Cannot run scan.")
        return

    send_log("Scanning for nearby networks...")
    # The scan itself can take a few seconds
    networks_found = sta_if.scan()
    send_log(f"Found {len(networks_found)} networks.")

    # Prepare the structured data for the app
    results_payload = {"type": "wifi_scan_results", "networks": []}
    for ssid, bssid, channel, rssi, authmode, hidden in networks_found:
        results_payload["networks"].append({
            "ssid": ssid.decode('utf-8', 'ignore'),
            "rssi": rssi,
            "bssid": ubinascii.hexlify(bssid, ':').decode(),
            "channel": channel
        })

    # Send the final result object back to the app using the RESULT: prefix
    send_log("RESULT:" + ujson.dumps(results_payload))

# --- Main execution of this script ---
try:
    run_scan()
    send_log("--- Scan Complete ---")
except Exception as e:
    send_log(f"Script Error: {e}")
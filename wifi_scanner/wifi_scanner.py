# This script runs on the DeZer0 device

# The firmware automatically provides the 'send_log' function.
# We don't need to import it.

send_log("--- Wi-Fi Scanner Tool Initialized ---")

def run_scan():
    """Scans for networks and sends results back to the app."""
    
    # The firmware provides 'network' and 'ujson' to the script
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        send_log("Error: Not connected to Wi-Fi.")
        return

    send_log("Scanning for Wi-Fi networks...")
    networks_found = sta_if.scan()
    send_log(f"Found {len(networks_found)} networks.")

    # We send results back to the app by printing a formatted JSON string.
    results = {"type": "wifi_scan_results", "networks": []}
    for ssid, bssid, channel, rssi, authmode, hidden in networks_found:
        results["networks"].append({"ssid": ssid.decode('utf-8', 'ignore'), "rssi": rssi})

    # Send the final result object back to the app using the RESULT: prefix
    send_log("RESULT:" + ujson.dumps(results))

# --- Main execution of this script ---
try:
    run_scan()
    send_log("--- Scan Complete ---")
except Exception as e:
    send_log(f"Script Error: {e}")
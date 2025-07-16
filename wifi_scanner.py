import network
import ujson
import time

# This script runs on the DeZer0 device after being sent from the app.

print("--- Wi-Fi Scanner Tool Loaded ---")

def run_scan():
    """Scans for networks and prints results as JSON."""
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Error: Not connected to Wi-Fi.")
        return

    print("Scanning for Wi-Fi networks...")
    networks_found = sta_if.scan()
    print(f"Found {len(networks_found)} networks.")

    # We send results back to the app by printing a formatted JSON string.
    # The app will listen for any line that starts with "RESULT:"
    results = {"type": "wifi_scan_results", "networks": []}
    for ssid, bssid, channel, rssi, authmode, hidden in networks_found:
        results["networks"].append({"ssid": ssid.decode('utf-8', 'ignore'), "rssi": rssi})

    print("RESULT:" + ujson.dumps(results))

# --- Main execution of this script ---
run_scan()
print("--- Scan Complete ---")
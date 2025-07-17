# wifi_scanner.py
# This script uses the standard print() function.
# The DeZer0 firmware will redirect all its output to the app.

import network
import ujson
import time

print("--- Wi-Fi Scanner Tool Initialized ---")

def run_scan():
    """Scans for networks and prints results as JSON."""
    
    sta_if = network.WLAN(network.STA_IF)
    
    if not sta_if.isconnected():
        print("Error: Wi-Fi is disconnected.")
        return

    print("Scanning for nearby networks...")
    networks_found = sta_if.scan()
    print(f"Found {len(networks_found)} networks.")

    results_payload = {"type": "wifi_scan_results", "networks": []}
    for ssid, bssid, channel, rssi, authmode, hidden in networks_found:
        results_payload["networks"].append({
            "ssid": ssid.decode('utf-8', 'ignore'),
            "rssi": rssi
        })

    # Send the final result object back to the app by printing it with a prefix
    print("RESULT:" + ujson.dumps(results_payload))

# --- Main execution of this script ---
try:
    run_scan()
    print("--- Scan Complete ---")
except Exception as e:
    print(f"Script Error: {e}")
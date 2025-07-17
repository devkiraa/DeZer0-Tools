# wifi_scanner.py - Final Version

# The main firmware provides these modules to the script's environment.
# We only need to import them if we use them inside functions.

def run_scan():
    """Scans for networks and sends results back to the app."""
    import network
    import ujson

    print("--- Wi-Fi Scanner Tool Initialized ---")
    
    sta_if = network.WLAN(network.STA_IF)
    
    if not sta_if.isconnected():
        print("Error: Wi-Fi is disconnected.")
        return

    print("Scanning for nearby networks...")
    networks_found = sta_if.scan()
    print(f"Found {len(networks_found)} networks.")

    # Prepare the structured data for the app
    results_payload = {"type": "wifi_scan_results", "networks": []}
    for ssid, bssid, channel, rssi, authmode, hidden in networks_found:
        results_payload["networks"].append({
            "ssid": ssid.decode('utf-8', 'ignore'),
            "rssi": rssi
        })

    # Send the final result object back to the app using the RESULT: prefix
    print("RESULT:" + ujson.dumps(results_payload))

# --- Main execution of this script ---
try:
    run_scan()
    print("--- Scan Complete ---")
except Exception as e:
    print(f"Script Error: {e}")

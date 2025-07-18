# wifi_scanner.py
# This script defines a run_tool() function and executes it
# Output is printed so the ESP32 server can capture it

import network
import ujson

def run_tool():
    """Scans for networks and returns a formatted string with all logs and results."""
    
    output_lines = []
    output_lines.append("--- Wi-Fi Scanner Tool Initialized ---")
    
    sta_if = network.WLAN(network.STA_IF)
    
    if not sta_if.isconnected():
        output_lines.append("Error: Wi-Fi is disconnected.")
        return "\n".join(output_lines)

    output_lines.append("Scanning for nearby networks...")
    networks_found = sta_if.scan()
    output_lines.append(f"Found {len(networks_found)} networks.")

    results_payload = {"type": "wifi_scan_results", "networks": []}
    for ssid, bssid, channel, rssi, authmode, hidden in networks_found:
        results_payload["networks"].append({
            "ssid": ssid.decode('utf-8', 'ignore'),
            "rssi": rssi
        })

    output_lines.append("RESULT: " + ujson.dumps(results_payload))
    output_lines.append("--- Scan Complete ---")
    
    return "\n".join(output_lines)

# Ensure the script runs when executed via exec()
if __name__ == "__main__":
    result = run_tool()
    print(result)
    print()  # Ensure final newline
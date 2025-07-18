# wifi_scanner.py - Return-based version
# This script does not use print() for communication.

import network
import ujson

def run_tool():
    """Scans for networks and returns a formatted string with all logs and results."""
    
    # Use a list to collect all output lines
    output_lines = []
    output_lines.append("--- Wi-Fi Scanner Tool Initialized ---")
    
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        output_lines.append("Error: Wi-Fi is disconnected.")
        return "\n".join(output_lines)

    output_lines.append("Scanning for nearby networks...")
    networks_found = sta_if.scan()
    output_lines.append(f"Found {len(networks_found)} networks.")

    # Prepare the structured data
    results_payload = {"type": "wifi_scan_results", "networks": []}
    for ssid, bssid, channel, rssi, authmode, hidden in networks_found:
        results_payload["networks"].append({
            "ssid": ssid.decode('utf-8', 'ignore'),
            "rssi": rssi
        })

    # Add the final result object to our output using the RESULT: prefix
    output_lines.append("RESULT:" + ujson.dumps(results_payload))
    output_lines.append("--- Scan Complete ---")
    
    # Return all the collected lines, joined together by newlines
    return "\n".join(output_lines)

# The firmware will call the run_tool() function, so no other code is needed here.
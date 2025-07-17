import bluetooth
import ujson
import time

# This script runs on the DeZer0 device

print("--- BLE Scanner Tool Initialized ---")

def run_scan():
    """Scans for BLE devices and prints results as JSON."""
    print("Scanning for Bluetooth Low Energy devices...")
    
    # Start scanning for BLE devices
    ble_devices = bluetooth.discover_devices(duration=8, lookup_names=True)
    print(f"Found {len(ble_devices)} devices.")

    results_payload = {"type": "ble_scan_results", "devices": []}
    for addr, name in ble_devices:
        results_payload["devices"].append({"address": addr, "name": name})

    # Send the final result object back to the app using the RESULT: prefix
    print("RESULT:" + ujson.dumps(results_payload))

# --- Main execution of this script ---
try:
    run_scan()
    print("--- Scan Complete ---")
except Exception as e:
    print(f"Script Error: {e}")
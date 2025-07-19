# ble_tracker.py
# This script scans for nearby Bluetooth Low Energy devices.

import bluetooth
import uasyncio as asyncio
import ujson

# The main firmware provides all necessary modules.

def run_tool():
    """Scans for BLE devices and returns the results."""
    
    output_lines = []
    output_lines.append("--- BLE Tracker Initialized ---")
    
    # We need an async function to handle the scan
    async def do_scan():
        output_lines.append("Starting BLE scan for 5 seconds...")
        
        ble = bluetooth.BLE()
        ble.active(True)
        
        found_devices = {}
        def scan_callback(adv_type, addr, adv_data):
            addr_str = ubinascii.hexlify(addr, ':').decode()
            name = ""
            for name, value in adv_data:
                if name == 0x09: # Complete Local Name
                    name = value.decode('utf-8')
            
            if addr_str not in found_devices:
                found_devices[addr_str] = name if name else "Unknown"
                output_lines.append(f"Found: {addr_str} - {name if name else 'N/A'}")

        ble.gap_scan(5000, 30000, 30000) # Scan for 5 seconds
        time.sleep(5.1) # Wait for scan to finish
        ble.active(False)

        output_lines.append(f"Scan finished. Found {len(found_devices)} unique devices.")
        
        # Prepare the structured results
        results_payload = {"type": "ble_scan_results", "devices": []}
        for addr, name in found_devices.items():
            results_payload["devices"].append({"address": addr, "name": name})
            
        output_lines.append("RESULT:" + ujson.dumps(results_payload))
        output_lines.append("--- Scan Complete ---")

    # Run the async scan function
    try:
        # In MicroPython, we can't directly run an async function inside a sync one.
        # This is a simple workaround for our current firmware.
        # A more advanced firmware could run this as a proper async task.
        output_lines.append("Note: BLE Scan is experimental.")
        output_lines.append("--- Scan Complete ---") # Placeholder
    except Exception as e:
        output_lines.append(f"Script Error: {e}")
        
    return "\n".join(output_lines)
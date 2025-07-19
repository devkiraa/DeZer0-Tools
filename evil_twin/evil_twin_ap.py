# evil_twin_ap.py
# Creates a fake Wi-Fi Access Point.

import network
import time

# --- Parameters ---
# In a future version, the app could send these as arguments.
TARGET_SSID = "Free_Public_WiFi"
# ------------------

def run_tool():
    """Creates a fake AP and reports its status."""
    
    output_lines = []
    output_lines.append("--- Evil Twin AP Initialized ---")

    ap_if = network.WLAN(network.AP_IF)
    
    try:
        output_lines.append(f"Starting AP with SSID: {TARGET_SSID}")
        ap_if.config(essid=TARGET_SSID, password="") # Open network
        ap_if.active(True)
        
        # Wait a moment for the AP to start
        time.sleep(2)

        if ap_if.active():
            output_lines.append("✅ Success! Evil Twin is now broadcasting.")
            output_lines.append(f"SSID: {ap_if.config('essid')}")
            output_lines.append("Note: This will stop when you run another tool or disconnect.")
        else:
            output_lines.append("❌ Error: Failed to start Access Point.")

    except Exception as e:
        output_lines.append(f"Script Error: {e}")
    finally:
        # In this simple version, the AP stays active.
        # A more advanced tool could run a web server or stop after a timeout.
        pass

    return "\n".join(output_lines)
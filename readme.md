# DeZer0 Community Tools

This repository is the official collection of tools and packages for the **DeZer0** platform. Each tool is a self-contained MicroPython script designed to be downloaded and executed by the DeZer0 companion app.

## How to Create a New Tool

To create a new tool compatible with the DeZer0 platform, you must create a new folder in the root of this repository. This folder must contain two essential files:

1.  `manifest.json`: A file containing the metadata for your tool.
2.  `<tool_id>.py`: The main Python script to be executed on the ESP32. The filename must match the `id` in your manifest.

### 1\. The `manifest.json` File

This file describes your tool to the marketplace in the DeZer0 app. It must contain the following fields:

```json
{
  "id": "wifi_scanner",
  "name": "Wi-Fi Scanner",
  "author": "YourGitHubUsername",
  "version": "v1.0",
  "category": "Wi-Fi",
  "size": "2 KiB",
  "description": "A brief, one-sentence description of what your tool does.",
  "script_filename": "wifi_scanner.py",
  "changelog": "v1.0 - Initial release."
}
```

**Field Explanations:**

  * **`id`**: A unique, lowercase identifier for your tool using underscores (`_`) instead of spaces. **The main python script must have this name.** (e.g., `wifi_scanner.py`).
  * **`name`**: The human-readable display name for your tool.
  * **`author`**: Your name or username.
  * **`version`**: The current version of your tool (e.g., "v1.0", "v1.0.1").
  * **`category`**: The category your tool belongs to (e.g., "Wi-Fi", "Bluetooth", "GPIO", "Tools").
  * **`size`**: The approximate size of your script file (e.g., "2 KiB", "15 KiB").
  * **`description`**: A short description displayed in the marketplace list.
  * **`script_filename`**: The exact filename of your Python script.
  * **`changelog`**: A string containing notes for the latest version.

### 2\. The Python Script (`<tool_id>.py`)

This is the code that will be sent to and executed by the ESP32. It must be written in **MicroPython**.

#### Communication Protocol

The script communicates back to the Flutter app by using the standard `print()` function. The app's console will display everything your script prints.

  * **For regular logs:** Use a simple `print()` statement.
    ```python
    print("Starting network scan...")
    ```
  * **To send structured data back (like scan results):** You must print a single line prefixed with `RESULT:`. The app specifically looks for this prefix to parse the line as JSON data.
    ```python
    import ujson

    # ... your logic to get data ...

    my_data = {"type": "scan_results", "networks": ["net1", "net2"]}

    # Send the final result back to the app
    print("RESULT:" + ujson.dumps(my_data))
    ```

#### Script Best Practices

  * Your script should be self-contained. Assume only the standard MicroPython libraries are available.
  * Use `try...except` blocks to handle potential errors gracefully.
  * Provide clear `print()` statements to log the script's progress.
  * Keep the script as small and efficient as possible.

-----

### \#\# Example Tool: Wi-Fi Scanner

Here is a complete, working example for a `wifi_scanner` tool.

#### Folder Structure:

```
DeZer0-Tool-Hub/
└── wifi_scanner/
    ├── manifest.json
    └── wifi_scanner.py
```

#### `wifi_scanner/manifest.json`:

```json
{
  "id": "wifi_scanner",
  "name": "Wi-Fi Scanner",
  "author": "DeZer0 Team",
  "version": "v1.0",
  "category": "Wi-Fi",
  "size": "2 KiB",
  "description": "Scans for nearby 2.4GHz Wi-Fi networks and displays the results.",
  "script_filename": "wifi_scanner.py",
  "changelog": "v1.0 - Initial release."
}
```

#### `wifi_scanner/wifi_scanner.py`:

```python
import network
import ujson
import time

# This script runs on the DeZer0 device

print("--- Wi-Fi Scanner Tool Initialized ---")

def run_scan():
    """Scans for networks and prints results as JSON."""
    sta_if = network.WLAN(network.STA_IF)
    
    # Ensure the interface is active before scanning
    if not sta_if.active():
        sta_if.active(True)

    print("Scanning for Wi-Fi networks...")
    networks_found = sta_if.scan()
    print(f"Found {len(networks_found)} networks.")

    results_payload = {"type": "wifi_scan_results", "networks": []}
    for ssid, bssid, channel, rssi, authmode, hidden in networks_found:
        results_payload["networks"].append({"ssid": ssid.decode('utf-8', 'ignore'), "rssi": rssi})

    # Send the final result object back to the app using the RESULT: prefix
    print("RESULT:" + ujson.dumps(results_payload))

# --- Main execution of this script ---
try:
    run_scan()
    print("--- Scan Complete ---")
except Exception as e:
    print(f"Script Error: {e}")
```
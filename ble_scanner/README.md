# BLE Scanner Tool

This repository contains the Bluetooth Low Energy (BLE) Scanner tool for the DeZer0 platform. This tool is designed to scan for nearby BLE devices and communicate the results back to the DeZer0 companion app.

## Features

- Scans for nearby Bluetooth Low Energy devices.
- Displays the results in a structured format.
- Easy integration with the DeZer0 platform.

## How to Use

1. **Setup**: Ensure your ESP32 device is properly configured and connected to the DeZer0 companion app.
2. **Run the Tool**: Execute the `ble_scanner.py` script on your ESP32 device.
3. **View Results**: The results of the scan will be printed to the app's console, prefixed with `RESULT:` for easy parsing.

## File Structure

```
ble_scanner/
├── manifest.json
├── ble_scanner.py
└── README.md
```

## Additional Information

For more details on how to create and manage tools for the DeZer0 platform, refer to the official documentation provided in the repository.
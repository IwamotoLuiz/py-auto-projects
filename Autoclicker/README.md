---

# Autoclicker

## Description
This basic Python script enables an autoclicker functionality, allowing users to automate mouse clicks at a specified frequency. The autoclicker can be toggled on/off using a designated hotkey and exited with another hotkey.

## Dependencies
- `pyautogui`: Python module for GUI automation
- `keyboard`: Python module for detecting keyboard events
- `threading`: Python module for concurrent execution

## Usage
1. Install the required dependencies using pip:
    ```
    pip install pyautogui keyboard
    ```

2. Run the script:
    ```
    python autoclicker.py
    ```

3. Press the specified hotkey (default: F2) to toggle the autoclicker on/off.
   
4. Press the specified exit key (default: esc) to exit the application.

## Configuration
- `on_off_key`: Defines the hotkey to start/stop the autoclicker.
- `exit_key`: Defines the hotkey to exit the application.
- `click_delay`: Specifies the delay between consecutive clicks (in seconds). Adjust as needed for desired click frequency.

## Notes
- Ensure that the mouse cursor is positioned appropriately before toggling the autoclicker.

---

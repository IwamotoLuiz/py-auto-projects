import pyautogui
import keyboard
import threading

autoclicker_active = False
autoclick_thread = None
click_delay = 0.00001

on_off_key = 'F2'  # defines which key starts/stops the autoclicker
exit_key = 'esc'  # defines which key exits the application


# toggles the autoclick on/off
def toggle_autoclick():
    global autoclicker_active
    autoclicker_active = not autoclicker_active
    autoclicker_state = 'OFF'
    if autoclicker_active:
        start_autoclicker()
        autoclicker_state = 'ON'
    else:
        stop_autoclicker()
    print(f'\rThe autoclicker is currently {autoclicker_state}', end='', flush=True)


# starts the autoclicker in a separated thread
def start_autoclicker():
    global autoclick_thread
    autoclick_thread = threading.Thread(target=autoclicker)
    autoclick_thread.start()


# stops the autoclicker ongoing thread
def stop_autoclicker():
    global autoclick_thread
    if autoclick_thread:
        autoclick_thread = None


# detects if the thread is active and gives the click command, if so
def autoclicker():
    while autoclicker_active:
        pyautogui.click()
        pyautogui.PAUSE = click_delay


print(f'> Press {on_off_key} to start/stop the autoclicker.')
print(f'> Press {exit_key} to exit.\n')

# assemble the 'toggle_autoclick' function to a key
keyboard.add_hotkey(on_off_key, toggle_autoclick)

# exits when a key is pressed
keyboard.wait(exit_key)

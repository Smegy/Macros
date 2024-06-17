import pyautogui
import keyboard


def on_keypad7_pressed():

    pyautogui.mouseDown(button='left')


# Listen for the keypad 8 key press
keyboard.add_hotkey('num 7', on_keypad7_pressed)

# Keep the script running to listen for the key press
print("Listening for keypad 7 press... (Press 4 to stop)")
keyboard.wait('4')

import pyautogui
import keyboard


def on_keypad9_pressed():
    # Press the letter T
    pyautogui.press('t')
    # Type '/spawn'
    pyautogui.typewrite('/spawn')
    # Press the Enter key on the keypad
    pyautogui.press('enter')


def on_keypad7_pressed():
        # Press the letter T
        pyautogui.mouseDown(button='left')


# Listen for the keypad 8 key press
keyboard.add_hotkey('num 9', on_keypad9_pressed)
keyboard.add_hotkey('num 7', on_keypad7_pressed)


# Keep the script running to listen for the key press
print("Listening for keypad 9 press... Mine (Press 7 to stop)")
keyboard.wait('7')
pyautogui.mouseUp(button='left')


#

import pyautogui
import keyboard


def on_keypad8_pressed():
    # Press the letter T
    pyautogui.press('t')
    # Type '/spawn'
    pyautogui.typewrite('/spawn')
    # Press the Enter key on the keypad
    pyautogui.press('enter')

# Listen for the keypad 8 key press
keyboard.add_hotkey('num 9', on_keypad8_pressed)


# Keep the script running to listen for the key press
print("Listening for keypad 9 press... (Press 8 to stop)")
keyboard.wait('8')


#

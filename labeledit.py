import pyautogui
import keyboard
while True:
    k = keyboard.read_key()
    #h = keyboard.read_hotkey()
    if k == 'f1':
        pyautogui.hotkey('ctrl', 'e')
        pyautogui.typewrite('person')
        pyautogui.press('enter')
        pyautogui.press('enter')
    elif k == 'f2':
        pyautogui.hotkey('ctrl', 'e')
        pyautogui.typewrite('truck')
        pyautogui.press('enter')
        pyautogui.press('enter')
    elif k == 'f3':
        pyautogui.hotkey('ctrl', 'e')
        pyautogui.typewrite('bus')
        pyautogui.press('enter')
        pyautogui.press('enter')
    elif k == 'f':
        pyautogui.keyDown('ctrl')
        pyautogui.scroll(5500)
        pyautogui.keyUp('ctrl')
    elif k == 'g':
        pyautogui.keyDown('ctrl')
        pyautogui.scroll(-5500)
        pyautogui.keyUp('ctrl')
    elif k == 'f10':
        break

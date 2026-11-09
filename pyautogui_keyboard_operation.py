import pyautogui
import time
import pyscreeze
'''
pyautogui.typewrite("Hello, World!", interval=0.1)
#hot keys
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'x')
pyautogui.hotkey('ctrl', 'z')

#pressing special keys

pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('backspace')
 #holding down keys
pyautogui.keyDown('shift')  
pyautogui.typewrite("This text is in uppercase")
'''

screenshot = pyautogui.screenshot()
screenshot.save("final.png")
import pyautogui    
import time

#mouse operation
pyautogui.moveTo(100, 100, duration=1)
pyautogui.rightClick(100, 100)
pyautogui.leftClick(100, 100)
pyautogui.dragTo(200, 200, duration=1)
pyautogui.scroll(-10)
time.sleep(1)
pyautogui.scroll(10)
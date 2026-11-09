import pyautogui
import time

pyautogui.FAILSAFE = True

time.sleep(2)

pyautogui.moveTo(500, 300, duration=1)

print("Mouse automation completed!")
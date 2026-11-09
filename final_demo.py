import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

print("open the chrome browser")    
time.sleep(2)

pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.typewrite("chrome")
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)

print("go to the website")
pyautogui.hotkey('ctrl', 't', interval=0.25)
time.sleep(1)
pyautogui.typewrite("https://www.accuweather.com/en/in/mannargudi/190771/weather-forecast/190771?type=locality&city=mannargudi#google_vignette", interval=0.1)
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)

print("Step:3 Copy the Full webstie")
pyautogui.hotkey('ctrl', 'a', interval=0.25)
time.sleep(1)
pyautogui.hotkey('ctrl', 'c', interval=0.25)
time.sleep(1)
# Step 4: Open Notepad
print("Step 4: Open Notepad")

# Open Windows Run dialog
pyautogui.hotkey('win', 'r', interval=0.25)
time.sleep(2)

# Type Notepad
pyautogui.write('notepad', interval=0.1)
time.sleep(1)

# Open Notepad
pyautogui.press('enter')
time.sleep(3)


# Step 5: Paste the Copied Content
print("Step 5: Paste the Website Content")

pyautogui.hotkey('ctrl', 'v', interval=0.25)
time.sleep(2)

print("Website content pasted successfully!")

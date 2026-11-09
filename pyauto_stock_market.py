import pyautogui
import pyperclip
import time
import os
from datetime import datetime

# ==========================================
# STOCK MARKET AUTOMATION USING PYAUTOGUI
# ==========================================

# Screen automation settings
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

# Get today's date and time
now = datetime.now()

date_time = now.strftime("%d-%m-%Y %H:%M:%S")

file_time = now.strftime("%d-%m-%Y_%H-%M-%S")

# Create output folder
output_folder = "Stock_Market_Reports"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Excel file name
excel_file = os.path.abspath(
    os.path.join(
        output_folder,
        f"Stock_Market_Report_{file_time}.xlsx"
    )
)

# Screenshot file name
screenshot_file = os.path.abspath(
    os.path.join(
        output_folder,
        f"Stock_Market_Screenshot_{file_time}.png"
    )
)

# ==========================================
# STEP 1: OPEN GOOGLE CHROME
# ==========================================

print("Step 1: Opening Google Chrome")

pyautogui.hotkey("win", "r")
time.sleep(2)

pyautogui.write("chrome", interval=0.1)
pyautogui.press("enter")

time.sleep(5)

# ==========================================
# STEP 2: OPEN STOCK MARKET WEBSITE
# ==========================================

print("Step 2: Opening Stock Market Website")

website_url = "https://www.moneycontrol.com/news/business/markets/"

pyautogui.hotkey("ctrl", "l")
pyautogui.write(website_url, interval=0.03)
pyautogui.press("enter")

time.sleep(10)

# ==========================================
# STEP 3: COPY IMPORTANT STOCK MARKET UPDATES
# ==========================================

print("Step 3: Copying Stock Market Updates")

pyautogui.hotkey("ctrl", "a")
time.sleep(2)

pyautogui.hotkey("ctrl", "c")
time.sleep(3)

# Read copied website text from clipboard
website_data = pyperclip.paste()

# Clean the copied text
website_data = website_data.strip()

# Limit the text to avoid excessive content
important_data = website_data[:1500]

if not important_data:
    important_data = "No stock market updates fetched."

print("Stock Market Data:")
print(important_data)

# ==========================================
# STEP 4: CREATE SHORT COMMENT
# ==========================================

print("Step 4: Creating Short Comment")

comment = "Stock market updates collected for daily analysis."

# ==========================================
# STEP 5: OPEN MICROSOFT EXCEL
# ==========================================

print("Step 5: Opening Microsoft Excel")

pyautogui.hotkey("win", "r")
time.sleep(2)

pyautogui.write("excel", interval=0.1)
pyautogui.press("enter")

time.sleep(8)

# ==========================================
# STEP 6: CREATE NEW EXCEL WORKBOOK
# ==========================================

print("Step 6: Creating New Excel Workbook")

pyautogui.hotkey("ctrl", "n")
time.sleep(5)

# ==========================================
# STEP 7: INSERT DATA INTO EXCEL
# ==========================================

print("Step 7: Inserting Data into Excel")

# Header row
headers = [
    "Date & Time",
    "Stock Market Updates",
    "Comment"
]

# Insert headers
pyautogui.write(headers[0], interval=0.05)
pyautogui.press("tab")

pyautogui.write(headers[1], interval=0.05)
pyautogui.press("tab")

pyautogui.write(headers[2], interval=0.05)

pyautogui.press("enter")

# Insert data row
pyautogui.write(date_time, interval=0.05)
pyautogui.press("tab")

# Paste copied stock market data
pyperclip.copy(important_data)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

pyautogui.write(comment, interval=0.05)

# ==========================================
# STEP 8: FORMAT EXCEL SHEET
# ==========================================

print("Step 8: Formatting Excel Sheet")

# Select first row
pyautogui.hotkey("ctrl", "home")

pyautogui.hotkey("shift", "right")
pyautogui.hotkey("shift", "right")

pyautogui.hotkey("shift", "right")

# Bold headers
pyautogui.hotkey("ctrl", "b")

# Select entire worksheet
pyautogui.hotkey("ctrl", "a")

# Auto fit columns
pyautogui.hotkey("alt", "h")
pyautogui.hotkey("o")
pyautogui.hotkey("i")

time.sleep(3)

# ==========================================
# STEP 9: SAVE EXCEL FILE
# ==========================================

print("Step 9: Saving Excel File")

pyautogui.hotkey("ctrl", "shift", "s")

time.sleep(3)

# Enter Excel file path
pyautogui.hotkey("ctrl", "a")

pyperclip.copy(excel_file)
pyautogui.hotkey("ctrl", "v")

time.sleep(2)

pyautogui.press("enter")

time.sleep(5)

# Handle possible Excel format confirmation
pyautogui.press("enter")

time.sleep(3)

print("Excel File Saved Successfully!")

print("File Location:")
print(excel_file)

# ==========================================
# STEP 10: TAKE SCREENSHOT OF EXCEL
# ==========================================

print("Step 10: Taking Screenshot")

# Ensure Excel is visible
pyautogui.hotkey("alt", "tab")
time.sleep(3)

# Capture screenshot
screenshot = pyautogui.screenshot()

# Save screenshot
screenshot.save(screenshot_file)

print("Screenshot Saved Successfully!")

print("Screenshot Location:")
print(screenshot_file)

# ==========================================
# AUTOMATION COMPLETED
# ==========================================

print("------------------------------------")
print("STOCK MARKET AUTOMATION COMPLETED")
print("------------------------------------")

print("Date & Time:", date_time)
print("Excel File:", excel_file)
print("Screenshot:", screenshot_file)
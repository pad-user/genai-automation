from playwright.sync_api import sync_playwright
from datetime import datetime

print("Starting the Playwright automation script...")
start_time = datetime.now()

#Daily weather Report Bot 
#chromium --> weather site --> extract the report --> screenshot --> final text file
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.accuweather.com/en/in/mannargudi/190771/weather-forecast/190771?type=locality&city=mannargudi#google_vignette")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="weather-report.png")

    #clicking
    page.click("text=Hourly")
    page.screenshot(path="full-report.png")

    #typing
    page.fill("input[name='q']", "Playwright")
    page.press("input[name='q']", "Enter")
    page.screenshot(path="search-results.png")

    #waiting for elements
    page.wait_for_selector("text=Playwright: Fast and reliable end-to-end testing for modern web apps")
    page.screenshot(path="waited-results.png")

    #extracting the data
    title = page.title()
    print(f"Page title: {title}")
    
    #closing the browser
    browser.close()
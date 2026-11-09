from playwright.sync_api import sync_playwright
from datetime import datetime

print("Starting the Playwright automation script...")
start_time = datetime.now()

#Cricket Scrore Bot
#chromium --> cricket score site --> extract the score --> screenshot --> final text file
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.cricbuzz.com/cricket-match/live-scores")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="cricket-score.png")

    #clicking
    page.click("text=Live Scores")
    page.screenshot(path="full-score.png")

    #extracting the data
    title = page.title()
    print(f"Page title: {title}")
    
    #closing the browser
    browser.close()
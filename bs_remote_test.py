import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

USERNAME = os.getenv("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

if not USERNAME or not ACCESS_KEY:
    raise Exception("BrowserStack credentials not set")

URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

options = Options()
options.set_capability("browserName", "Chrome")
options.set_capability("browserVersion", "latest")
options.set_capability("bstack:options", {
    "os": "Windows",
    "osVersion": "11",
    "sessionName": "First Remote Test",
    "buildName": "Beginner to Tier-2"
})

driver = webdriver.Remote(
    command_executor=URL,
    options=options
)

driver.get("https://example.com")
print("Title is:", driver.title)
driver.quit()

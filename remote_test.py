from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 1. Tell Selenium we want Chrome
options = Options()
options.add_argument("--headless")

# 2. Connect to remote Selenium Grid
driver = webdriver.Remote(
    command_executor="https://demo.selenium.dev/wd/hub",
    options=options
)

# 3. Open a website
driver.get("https://example.com")

# 4. Find text on the page
title = driver.find_element(By.TAG_NAME, "h1").text
print("Page title is:", title)

# 5. Close browser
driver.quit()

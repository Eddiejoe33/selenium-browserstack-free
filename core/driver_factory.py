import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():
    username = os.getenv("BROWSERSTACK_USERNAME")
    access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")

    if not username or not access_key:
        raise Exception("BrowserStack credentials not set")

    options = Options()
    options.set_capability("browserName", "Chrome")
    options.set_capability("browserVersion", "latest")
    options.set_capability("platformName", "Windows 11")

    options.set_capability("bstack:options", {
        "userName": username,
        "accessKey": access_key,
        "sessionName": "Beginner Selenium Test",
        "buildName": "Selenium Learning Build"
    })

    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=options
    )

    return driver

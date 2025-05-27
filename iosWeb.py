from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

desired_caps = {
    "deviceName": "iPhone .*",
    "platformName": "ios",
    "platformVersion": "14",
    "isRealMobile": True,
    "build": "Python Vanilla iOS",
    "name": "Sample Test - Python",
    "network": False,
    "visual": True,
    "video": True
}


def startingTest():
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        options = XCUITestOptions()
        for key, value in desired_caps.items():
            options.set_capability(key, value)
        driver = webdriver.Remote(
            command_executor="https://" + username + ":" + accesskey + "@mobile-hub.lambdatest.com/wd/hub",
            options=options
        )

        driver.get("https://mfml.in/api/getInfo")
        time.sleep(3)
        print("Available contexts:", driver.contexts)
        
        # Wait for and click resolution
        resolution = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "resolution")))
        resolution.click()
        print("Clicked 'resolution' using Selenium.")

        # Wait for and click location
        location = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "location")))
        location.click()
        print("Clicked 'location' using Selenium.")

        # Wait for and click details
        details = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "details")))
        details.click()
        print("Clicked 'details' using Selenium.")

        # Wait for and click timezone
        timezone = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "timezone")))
        timezone.click()
        print("Clicked 'timezone' using Selenium.")

        driver.quit()
    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()

if __name__ == "__main__":
    startingTest()

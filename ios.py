from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.ios import XCUITestOptions
import time
import os

desired_caps = {
    "deviceName": "iPhone 12",
    "platformName": "iOS",
    "platformVersion": "14",
    "isRealMobile": True,
    "app": "lt://proverbial-ios",  # Enter app_url here
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

    driver = None
    try:
        options = XCUITestOptions()
        for key, value in desired_caps.items():
            options.set_capability(key, value)
            
        driver = webdriver.Remote(
            command_executor="https://" + username + ":" + accesskey + "@mobile-hub.lambdatest.com/wd/hub",
            options=options
        )
        colorElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "color")))
        colorElement.click()

        textElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text")))
        textElement.click()

        toastElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "toast")))
        toastElement.click()

        notification = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "notification")))
        notification.click()

        geolocation = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "geoLocation")))
        geolocation.click()
        time.sleep(15)

        driver.back()

        home = WebDriverWait(driver, 30, poll_frequency=1, ignored_exceptions=[Exception]).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Home"))
        )
        home.click()

        speedTest = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "speedTest")))
        speedTest.click()
        time.sleep(5)

        driver.back()

        browser = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "Browser")))
        browser.click()

        url = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "url")))
        url.send_keys("https://www.lambdatest.com")

        find = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "find")))
        find.click()
        driver.quit()
    except Exception as e:
        if driver:
            driver.quit()
        print(f"Test failed: {e}")

if __name__ == "__main__":
    startingTest()

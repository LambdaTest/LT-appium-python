from appium import webdriver
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

desired_caps = {
    "deviceName": "Galaxy .*",
    "platformName": "Android",
    "platformVersion": "10",
    "isRealMobile": True,
    "build": "Python Vanilla Android",
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
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  username+":"+accesskey+"@mobile-hub.lambdatest.com/wd/hub")

        driver.get("https://mfml.in/api/getInfo")
        colorElement = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.ID, "resolution")))
        colorElement.click()

        textElement = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "location")))
        textElement.click()

        toastElement = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.ID, "details")))
        toastElement.click()

        notification = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.ID, "timezone")))
        notification.click()

        time.sleep(5)

        driver.quit()
    except:
        driver.quit()


startingTest()

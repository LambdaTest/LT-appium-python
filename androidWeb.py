from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
import os

desired_caps = {
    "deviceName": "Galaxy .*",
    "platformName": "Android",
    "platformVersion": "14",
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
        options = UiAutomator2Options()
        for key, value in desired_caps.items():
            options.set_capability(key, value)
        driver = webdriver.Remote(
            command_executor="https://" + username + ":" + accesskey + "@mobile-hub.lambdatest.com/wd/hub",
            options=options
        )

        driver.get("https://mfml.in/api/getInfo")
        time.sleep(3)
        print("Available contexts:", driver.contexts)
        
        try:
            driver.execute_script('document.getElementById("resolution").click();')
            print("Clicked 'resolution' using JS.")
            driver.execute_script('document.getElementById("location").click();')
            print("Clicked 'location' using JS.")
            driver.execute_script('document.getElementById("details").click();')
            print("Clicked 'details' using JS.")
            driver.execute_script('document.getElementById("timezone").click();')
            print("Clicked 'timezone' using JS.")
        except Exception as js_e:
            print(f"JS click failed: {js_e}")

        driver.quit()
    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()

if __name__ == "__main__":
    startingTest()

"""
    This file contains the code to interact with generic parts of websites.
    For example: Extracting elements when they load, clicking buttons,
    pressing keys, scrolling, and submitting text.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import random

class WebAutomation:
    def __init__(self, chrome_driver_path, chrome_options = None):
        self.driver_path = chrome_driver_path  # Full path to the chrome driver

        # Configure options for Chrome
        if chrome_options:
            # If options are provided, use them
            self.options = chrome_options
        else:
            # Otherwise just use default options.
            self.options = Options()
        
        # Initiates the web driver
        self.driver = webdriver.Chrome(self.driver_path, chrome_options=self.options)

        # Number of seconds the driver will wait while finding an element before it stops
        self.driver_timeout = 30

    def get_by_xpath_wait(self, xpath):
        """
        Waits for an element with the provided XPath to load, when it loads return it.
        """
        return WebDriverWait(self.driver, self.driver_timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    
    # Get all elements of xpath when they load
    def get_all_by_xpath_wait(self, xpath):
        """
        Waits for elements with the provided XPath to load, when they load return them in a list.
        """
        return WebDriverWait(self.driver, self.driver_timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
    
    def refresh_page(self):
        """
        Refreshes the current page.
        """
        self.driver.get(self.driver.current_url)

    # Scrolls by a specified amount
    def scroll(self, amount):
        """
        Scrolls a specified amount in pixels.
        """
        self.driver.execute_script("window.scrollBy(0, " + str(amount) + ")")

    def simulate_typing(self, element, text):
        """
        Simulates a human typing text into an input.
        """
        for char in text:
            element.send_keys(char)

            # Pause for a fraction of a second to make it seem to the website like a human is typing
            random_pause = random.randint(1, 8) / 10
            time.sleep(random_pause)

    def quit(self):
        """
        Close the browser.
        """
        self.driver.quit()

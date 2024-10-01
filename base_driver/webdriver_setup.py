from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverSetup:
    def __init__(self):
        self.driver = None

    def start_browser(self):
        # Use ChromeDriver to initiate the browser
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        return self.driver

    def close_browser(self):
        if self.driver:
            self.driver.quit()

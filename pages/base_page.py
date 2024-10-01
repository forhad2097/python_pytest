from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).text

    def scroll_to_element(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def select_value_from_dropdown(self, by_locator, value):
        try:
            dropdown_element = self.driver.find_element(*by_locator)
            select = Select(dropdown_element)
            select.select_by_visible_text(value)
            print(f'Selected "{value}" from the dropdown.')
        except Exception as e:
            print(f"Error selecting value from dropdown: {e}")


    def search_element_by_search_box(self):
        def search_for_item(self, item_name):
            search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
            search_box.clear()
            search_box.send_keys(item_name)
            search_box.submit()

    def take_screenshot(self, filename="screenshot"):
        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
        file_path = os.path.join(screenshots_dir, f"{filename}_{timestamp}.png")  # Save in the 'screenshots' folder
        self.driver.save_screenshot(file_path)
        print(f"Screenshot saved at: {file_path}")
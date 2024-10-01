from selenium.webdriver.common.by import By
from utilities.common_methods import CommonMethods

class AmazonHomePage(CommonMethods):
    # Locators
    DEPARTMENT_DROPDOWN = (By.XPATH, "//select[@id='searchDropdownBox']")
    SOFTWARE_OPTION = (By.XPATH, "//option[text()='Software']")
    SEARCH_BAR = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.XPATH, "//input[@id='nav-search-submit-button']")
    POP_UP_DISMISS = (By.XPATH, "//input[@data-action-params='{\"toasterType\":\"AIS_INGRESS\"}']")

    def close_pop_up(self):
        try:
            self.click(self.POP_UP_DISMISS)
            print("Pop-up closed successfully.")
        except Exception as e:
            print("No pop-up appeared or pop-up was already handled")

    def select_software_in_dropdown(self):
        self.close_pop_up()
        self.select_value_from_dropdown(self.DEPARTMENT_DROPDOWN, "Software")

    def search_element_by_search_box(self, item_name):
        try:
            search_bar = self.driver.find_element(*self.SEARCH_BAR)
            search_bar.clear()
            search_bar.send_keys(item_name)
            search_bar.submit()
            self.take_screenshot("test_search_for_games_pass")
        except Exception as e:
            self.take_screenshot("test_search_for_games_fail")
import pytest
# In tests/test_amazon.py
from base_driver.webdriver_setup import *
from pages.amazon_home_page import AmazonHomePage

class TestAmazon:
    @pytest.fixture(scope="class")
    def setup(self):
        # Initialize the WebDriver and load the Amazon homepage
        self.driver_setup = WebDriverSetup()
        self.driver = self.driver_setup.start_browser()
        self.driver.get("https://www.amazon.com/")
        self.amazon_home_page = AmazonHomePage(self.driver)  # Assigning the instance to the class variable
        yield self.amazon_home_page  # Yield the instance for use in tests
        self.driver_setup.close_browser()  # Ensure browser is closed after tests

    def test_select_software(self, setup):
        # Case 1: Select 'Software' in the dropdown
        setup.select_software_in_dropdown()  # Call the method to select 'Software'

    def test_search_for_games(self, setup):
        # Case 2: Search for 'games'
        setup.search_element_by_search_box("games")
        setup.take_screenshot("test_search_for_games_pass")

    def test_close_browser(self, setup):
        # Case 3: Browser should close automatically after test completion
        pass

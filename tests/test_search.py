import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobject.HomePage import HomePage
from pageobject.SearchPage import SearchPage
from pageobject.BaseTest import BaseTest

# @pytest.mark.usefixtures("setup_and_teardown") --- remove this when you introduce BaseTest to the TestSearch class
class TestSearch(BaseTest):
    
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        # self.driver.find_element(By.NAME, "search").send_keys("HP")
        # home_page.enter_product_into_search_box_field("HP")
        # self.driver.find_element(By.XPATH, "//span[@class='input-group-btn']/button").click()
        # search_page = home_page.click_search_button() #return SearchPage in the HomePage (pageobject) under click_search_button #first optimization
        search_page = home_page.search_for_a_product("HP")
        # search_page = SearchPage(self.driver)
        # assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
        assert search_page.display_status_of_hp_products()

    def test_search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        # self.driver.find_element(By.NAME, "search").send_keys("Honda")
        # home_page.enter_product_into_search_box_field("Honda")
        # self.driver.find_element(By.XPATH, "//span[@class='input-group-btn']/button").click()
        # search_page = home_page.click_search_button()
        search_page = home_page.search_for_a_product("Honda")
        # search_page = SearchPage(self.driver)
        expected_text = "There is no product that matches the search criteria."
        # assert self.driver.find_element(By.XPATH, "//div[@id='content']/p[2]").text.__eq__(expected_text)
        assert search_page.invalid_product_message().__eq__(expected_text)

    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        # self.driver.find_element(By.NAME, "search").send_keys("")
        # home_page.enter_product_into_search_box_field("")
        # self.driver.find_element(By.XPATH, "//span[@class='input-group-btn']/button").click()
        # search_page = home_page.click_search_button()
        search_page = home_page.search_for_a_product("")
        # search_page = SearchPage(self.driver)
        expected_text = "There is no product that matches the search criteria."
        # assert self.driver.find_element(By.XPATH, "//div[@id='content']/p[2]").text.__eq__(expected_text)
        assert search_page.invalid_product_message().__eq__(expected_text)

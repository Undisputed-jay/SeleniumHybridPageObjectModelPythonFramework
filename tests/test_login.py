import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobject.HomePage import HomePage
from pageobject.Login import Login
from pageobject.MyAccount import MyAccount
from pageobject.BaseTest import BaseTest

from utilities import ExcelUtils

# @pytest.mark.usefixtures("setup_and_teardown") --- remove this when you introduce BaseTest to the TestLogin class
class TestLogin(BaseTest):
    @pytest.mark.parametrize("email_address, password", ExcelUtils.get_data_from_excel(path = "ExcelFiles/tutorialsninja.xlsx", sheet_name = "LoginTest"))
    def test_login_with_valid_credentials(self, email_address, password): # pass the email address and password for the parametrize here
        home_page = HomePage(self.driver)
        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # home_page.click_on_myaccount_dropdown()
        #  self.driver.find_element(By.LINK_TEXT, "Login").click()
        # login_page = home_page.select_login_option()  #return Login in the HomePage (pageobject) under select_login_option #first optimization
        # login_page = Login(self.driver)
        # self.driver.find_element(By.ID, "input-email").send_keys("bayodele73@gmail.com")
        login_page = home_page.account_dropdown_n_select_login_option()
        # login_page.input_email_address("bayodele73@gmail.com")
        # self.driver.find_element(By.ID, "input-password").send_keys("12345")
        # login_page.input_password_address("12345")
        # self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        # my_account = login_page.click_login_button()
        my_account = login_page.input_email_n_password(email_address, password)
        # my_account = MyAccount(self.driver)
        # assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
        assert my_account.information_displayed()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # home_page.click_on_myaccount_dropdown()
        # self.driver.find_element(By.LINK_TEXT, "Login").click()
        # login_page = home_page.select_login_option()
        # login_page = Login(self.driver)
        # self.driver.find_element(By.ID, "input-email").send_keys("")
        login_page = home_page.account_dropdown_n_select_login_option()
        # login_page.input_email_address("")
        # self.driver.find_element(By.ID, "input-password").send_keys("12345")
        # login_page.input_password_address("12345")
        # self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        # login_page.click_login_button()
        login_page.input_email_n_password("", "12345")
        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        # assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(expected_warning)
        assert login_page.error_account_message().__contains__(expected_warning)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # home_page.click_on_myaccount_dropdown()
        # self.driver.find_element(By.LINK_TEXT, "Login").click()
        # login_page = home_page.select_login_option()
        # login_page = Login(self.driver)
        # self.driver.find_element(By.ID, "input-email").send_keys("bayodele73@gmail.com")
        login_page = home_page.account_dropdown_n_select_login_option()
        # login_page.input_email_address("bayodele73@gmail.com")
        # self.driver.find_element(By.ID, "input-password").send_keys("")
        # login_page.input_password_address("")
        # self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        # login_page.click_login_button()
        login_page.input_email_n_password("bayodele73@gmail.com", "")
        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        # assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(expected_warning)
        assert login_page.error_account_message().__contains__(expected_warning)

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # home_page.click_on_myaccount_dropdown()
        # self.driver.find_element(By.LINK_TEXT, "Login").click()
        # login_page = home_page.select_login_option()
        # login_page = Login(self.driver)
        # self.driver.find_element(By.ID, "input-email").send_keys("")
        login_page = home_page.account_dropdown_n_select_login_option()
        # login_page.input_email_address("")
        # self.driver.find_element(By.ID, "input-password").send_keys("")
        # login_page.input_password_address("")
        # self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        # login_page.click_login_button()
        login_page.input_email_n_password("", "")
        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        # assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(expected_warning)
        assert login_page.error_account_message().__contains__(expected_warning)

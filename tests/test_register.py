import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobject.HomePage import HomePage
from pageobject.RegisterPage import RegisterPage
from pageobject.AccountSuccess import AccountSuccess
from pageobject.BaseTest import BaseTest

from utilities import ExcelUtils

# @pytest.mark.usefixtures("setup_and_teardown") --- remove this when you introduce BaseTest to the TestRegister class
class TestRegister(BaseTest):
    
    def test_register_with_mandatory_field(self):
        home_page = HomePage(self.driver)
        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # home_page.click_on_myaccount_dropdown()
        # self.driver.find_element(By.LINK_TEXT, "Register").click()
        # register_page = home_page.select_register_option() #return RegisterPage in the HomePage (pageobject)
        # register_page = RegisterPage(self.driver)
        # self.driver.find_element(By.ID, "input-firstname").send_keys("muniru")
        register_page = home_page.myaccount_dropdown_n_select_register_option()
        # register_page.input_all_values("tunde", "qudus", self.test_generate_email_with_timestamp(), "12345678", "12345", "12345") #replace this
        register_page.input_all_values(
            ExcelUtils.get_cell_data(path = "ExcelFiles/tutorialsninja.xlsx", sheet_name= "RegisterTest",row_number= 2, column_number=1),
            ExcelUtils.get_cell_data(path = "ExcelFiles/tutorialsninja.xlsx", sheet_name= "RegisterTest",row_number= 2, column_number=2),
            self.test_generate_email_with_timestamp(), "12345678", "12345", "12345") # with this
        # register_page.input_first_name("tunde")
        # self.driver.find_element(By.ID, "input-lastname").send_keys("ambali")
        # register_page.input_last_name("qudus")
        # self.driver.find_element(By.ID, "input-email").send_keys(self.test_generate_email_with_timestamp())
        # register_page.input_email(self.test_generate_email_with_timestamp())
        # self.driver.find_element(By.ID, "input-telephone").send_keys("12345678")
        # register_page.input_telephone("12345678")
        # self.driver.find_element(By.ID, "input-password").send_keys("12345")
        # register_page.input_password("12345")
        # self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        # register_page.confirm_password("12345")
        # self.driver.find_element(By.NAME, "agree").click()
        register_page.radio_agree_terms()
        # self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        account_success = register_page.continue_button() #return AccountSuccess in the RegisterPage(pageobject) for this to work
        # account_success = AccountSuccess(self.driver)
        expected_message = "Your Account Has Been Created!"
        # assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_message)
        assert account_success.account_success_message().__eq__(expected_message)
        
    def test_register_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # home_page.click_on_myaccount_dropdown()
        # self.driver.find_element(By.LINK_TEXT, "Register").click()
        # register_page = home_page.select_register_option() #return RegisterPage in the HomePage (pageobject)
        # register_page = RegisterPage(self.driver)
        # self.driver.find_element(By.ID, "input-firstname").send_keys("muniru")
        register_page = home_page.myaccount_dropdown_n_select_register_option()
        register_page.input_all_values("mufu", "ambali", "mufuambali@gmail.com", "12345678", "12345", "12345")
        # register_page.input_first_name("muniru")
        # self.driver.find_element(By.ID, "input-lastname").send_keys("ambali")
        # register_page.input_last_name("ambali")
        # self.driver.find_element(By.ID, "input-email").send_keys("munirambali@gmailcom")
        # register_page.input_email("muniruambali@gmailcom")
        # self.driver.find_element(By.ID, "input-telephone").send_keys("12345678")
        # register_page.input_telephone("12345678")
        # self.driver.find_element(By.ID, "input-password").send_keys("12345")
        # register_page.input_password("12345")
        # self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        # register_page.confirm_password("12345")
        # self.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
        register_page.agree_to_newsletter()
        # self.driver.find_element(By.NAME, "agree").click()
        register_page.radio_agree_terms()
        # self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        account_success = register_page.continue_button() #return AccountSuccess in the RegisterPage(pageobject)
        # account_success = AccountSuccess(self.driver)
        expected_message = "Your Account Has Been Created!"
        # assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_message)
        assert account_success.account_success_message().__contains__(expected_message)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # home_page.click_on_myaccount_dropdown()
        # self.driver.find_element(By.LINK_TEXT, "Register").click()
        # register_page = home_page.select_register_option()
        # register_page = RegisterPage(self.driver)
        # self.driver.find_element(By.ID, "input-firstname").send_keys("muniru")
        register_page = home_page.myaccount_dropdown_n_select_register_option()
        register_page.input_all_values("muniru", "ambali", "muniruambali@gmail.com", "12345678", "12345", "12345")
        # register_page.input_first_name("muniru")
        # self.driver.find_element(By.ID, "input-lastname").send_keys("ambali")
        # register_page.input_last_name("ambali")
        # self.driver.find_element(By.ID, "input-email").send_keys("munirambali@gmailcom")
        # register_page.input_email("muniruambali@gmailcom")
        # self.driver.find_element(By.ID, "input-telephone").send_keys("12345678")
        # register_page.input_telephone("12345678")
        # self.driver.find_element(By.ID, "input-password").send_keys("12345")
        # register_page.input_password("12345")
        # self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        # register_page.confirm_password("12345")
        # self.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
        register_page.agree_to_newsletter()
        # self.driver.find_element(By.NAME, "agree").click()
        register_page.radio_agree_terms()
        # self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        register_page.continue_button()
        expected_warning = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div").text.__contains__(expected_warning)
        
    def test_without_providing_any_information(self):
        home_page = HomePage(self.driver)
        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # home_page.click_on_myaccount_dropdown()
        # self.driver.find_element(By.LINK_TEXT, "Register").click()
        # register_page = home_page.select_register_option()
        # register_page = RegisterPage(self.driver)
        # self.driver.find_element(By.ID, "input-firstname").send_keys("")
        register_page = home_page.myaccount_dropdown_n_select_register_option()
        register_page.input_all_values("", "", "", "", "", "")
        # register_page.input_first_name("")
        # self.driver.find_element(By.ID, "input-lastname").send_keys("")
        # register_page.input_last_name("")
        # self.driver.find_element(By.ID, "input-email").send_keys("")
        # register_page.input_email("")
        # self.driver.find_element(By.ID, "input-telephone").send_keys("")
        # register_page.input_telephone("")
        # self.driver.find_element(By.ID, "input-password").send_keys("")
        # register_page.input_password("")
        # self.driver.find_element(By.ID, "input-confirm").send_keys("")
        # register_page.confirm_password("")
        # self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        register_page.continue_button()
        expected_warning_message = "Warning: You must agree to the Privacy Policy!"
        # assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div").text.__contains__(expected_warning_message)
        assert register_page.privacy_policy_error_message().__contains__(expected_warning_message)
        expected_firstname_warnings = "First Name must be between 1 and 32 characters!"
        # assert self.driver.find_element(By.XPATH, "//fieldset[1]/div[@class='form-group required has-error'][1]/div/div").text.__eq__(expected_firstname_warnings)
        assert register_page.input_first_name_error_message().__eq__(expected_firstname_warnings)
        expected_lastname_warnings = "Last Name must be between 1 and 32 characters!"
        # assert self.driver.find_element(By.XPATH, "//fieldset[1]/div[@class='form-group required has-error'][2]/div/div").text.__eq__(expected_lastname_warnings)
        assert register_page.input_last_name_error_message().__eq__(expected_lastname_warnings)
        expected_email_warnings = "E-Mail Address does not appear to be valid!"
        # assert self.driver.find_element(By.XPATH, "//fieldset[1]/div[@class='form-group required has-error'][3]/div/div").text.__eq__(expected_email_warnings)
        assert register_page.input_email_error_message().__eq__(expected_email_warnings)
        expected_phone_warnings = "Telephone must be between 3 and 32 characters!"
        # assert self.driver.find_element(By.XPATH, "//fieldset[1]/div[@class='form-group required has-error'][4]/div/div").text.__eq__(expected_phone_warnings)
        assert register_page.input_phone_error_message().__eq__(expected_phone_warnings)
        expected_password_error = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH, "//fieldset[2]/div[@class='form-group required has-error']/div/div").text.__eq__(expected_password_error)
        assert register_page.input_password_error_message().__eq__(expected_password_error)

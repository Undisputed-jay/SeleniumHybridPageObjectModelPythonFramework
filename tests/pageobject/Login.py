from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pageobject.MyAccount import MyAccount
from pageobject.BaseClass import BaseClass

# class Login --- this was there before introducing the base class
class Login(BaseClass):
    
    def __init__(self, driver):
        super().__init__(driver) # self.driver = driver,  this changes to super() when we introduce baseclass here
        
        
    email_address_field_id = "input-email"
    password_address_field_id = "input-password"
    login_xpath = "//input[@value='Login']"
    account_error_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"
        
        
    def input_email_address(self, email_address):
        self.type(email_address, "email_address_field_id", self.email_address_field_id) # returning the type function of baseclass here: the 3 lines can be discarded
        # self.driver.find_element(By.ID, self.email_address_field_id).click()
        # self.driver.find_element(By.ID, self.email_address_field_id).clear()
        # self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email_address)
        
    def input_password_address(self, password_address):
        self.type(password_address, "password_address_field_id", self.password_address_field_id) # returning the type function of baseclass here: the 3 lines can be discarded
        # self.driver.find_element(By.ID, self.password_address_field_id).click()
        # self.driver.find_element(By.ID, self.password_address_field_id).clear()
        # self.driver.find_element(By.ID, self.password_address_field_id).send_keys(password_address)
        
    def click_login_button(self):
        self.element_click("login_xpath", self.login_xpath) # returning the "element_click" function of baseclass here: the 3 lines can be discarded
        # self.driver.find_element(By.XPATH, self.login_xpath).click()
        return MyAccount(self.driver)
        
    def error_account_message(self):
        return self.check_for_text("account_error_message_xpath", self.account_error_message_xpath) # returning the "check_for_text" function of baseclass here: the 3 lines can be discarded
        # return self.driver.find_element(By.XPATH, self.account_error_message_xpath).text
    
    # this is putting 3 functions in one
    def input_email_n_password(self, email_address, password_address):
        self.input_email_address(email_address)
        self.input_password_address(password_address)
        return self.click_login_button()
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pageobject.BaseClass import BaseClass

# class AccountSuccess --- this was there before introducing the base class
class AccountSuccess(BaseClass):
    
    def __init__(self, driver):
        super().__init__(driver) #self.driver = driver, this changes to super() when we introduce baseclass here
        
    account_success_xpath = "//div[@class='col-sm-9']/h1"
    
    def account_success_message(self):
        return self.check_for_text("account_success_xpath", self.account_success_xpath) # returning the "check_for_text" function from baseclass
        # return self.driver.find_element(By.XPATH, self.account_success_xpath).text
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pageobject.BaseClass import BaseClass

# class MyAccount --- this was there before introducing the base class
class MyAccount(BaseClass):
    
    def __init__(self, driver):
        super().__init__(driver) #self.driver = driver, this changes to super() when we introduce baseclass here
        
    page_information_linktext = "Edit your account information"
        
    def information_displayed(self):
        return self.check_if_displayed("page_information_linktext", self.page_information_linktext) # returning the "check_if_displayed" function from baseclass
        # return self.driver.find_element(By.LINK_TEXT, self.page_information_linktext).is_displayed()
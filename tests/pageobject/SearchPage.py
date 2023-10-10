from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobject.BaseClass import BaseClass

# class SearchPage --- this was there before introducing the base class
class SearchPage(BaseClass): #searchpage becomes a child of baseclass
    
    def __init__(self, driver):
        super().__init__(driver) # self.driver = driver,  this changes to super() when we introduce baseclass here
        
        # these are locators in the baseclass 
    valid_hp_product_linktext = "HP LP3065"
    invalid_product_message_xpath = "//div[@id='content']/p[2]"
        
    def display_status_of_hp_products(self):
        return self.check_if_displayed("valid_hp_product_linktext", self.valid_hp_product_linktext) # returning the "check_if_displayed" function from baseclass
        # return self.driver.find_element(By.LINK_TEXT, self.valid_hp_product_linktext).is_displayed()
    
    def invalid_product_message(self):
        return self.check_for_text("invalid_product_message_xpath", self.invalid_product_message_xpath)  # returning the "check_for_text" function from baseclass
        # return self.driver.find_element(By.XPATH, self.invalid_product_message_xpath).text
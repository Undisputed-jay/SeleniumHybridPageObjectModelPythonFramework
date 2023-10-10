from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pageobject.SearchPage import SearchPage
from pageobject.Login import Login
from pageobject.RegisterPage import RegisterPage
from pageobject.BaseClass import BaseClass

# class HomePage --- this was there before introducing the base class
class HomePage(BaseClass): #homepage becomes a child of baseclass
    
    def __init__(self, driver):
        super().__init__(driver) # self.driver = driver, this changes to super() when we introduce baseclass here
    
        # these are locators in the baseclass
    search_box_field_name = "search"
    search_button_xpath = "//span[@class='input-group-btn']/button"
    my_account_dropdown_xpath = "//span[text()='My Account']"
    login_option_linktext = "Login"
    register_option_linktext = "Register"
        
        # this functions will be text in the baseclass
    def enter_product_into_search_box_field(self, product_name):
        self.type(product_name, "search_box_field_name", self.search_box_field_name) # returning the type function of baseclass here: the 3 lines can be discarded
        # self.driver.find_element(By.NAME, self.search_box_field_name).click()
        # self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        # self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)
         
    def click_search_button(self):
        self.element_click("search_button_xpath", self.search_button_xpath) #returning the "element_click" function from baseclass
        # self.driver.find_element(By.XPATH, self.search_button_xpath).click() 
        return SearchPage(self.driver)
        
    def click_on_myaccount_dropdown(self):
        self.element_click("my_account_dropdown_xpath", self.my_account_dropdown_xpath) #returning the "element_click" function from baseclass
        # self.driver.find_element(By.XPATH, self.my_account_dropdown_xpath).click()
        
    def select_login_option(self):
        self.element_click("login_option_linktext", self.login_option_linktext) #returning the "element_click" function from baseclass
        # self.driver.find_element(By.LINK_TEXT, self.login_option_linktext).click()
        return Login(self.driver)
        
    def select_register_option(self):
        self.element_click("register_option_linktext", self.register_option_linktext) #returning the "element_click" function from baseclass
        # self.driver.find_element(By.LINK_TEXT, self.register_option_linktext).click()
        return RegisterPage(self.driver)
    
# this will cover for "enter_product_into_search_box_field" and the "click_search_button" function
    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_search_button()

    
    # this will cover for "click_on_myaccount_dropdown" and "select_login_option" function
    def account_dropdown_n_select_login_option(self):
        self.click_on_myaccount_dropdown()
        return self.select_login_option()
    
    def myaccount_dropdown_n_select_register_option(self):
        self.click_on_myaccount_dropdown()
        return self.select_register_option()
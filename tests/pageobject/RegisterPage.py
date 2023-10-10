from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pageobject.AccountSuccess import AccountSuccess
from pageobject.BaseClass import BaseClass

# class RegisterPage --- this was there before introducing the base class
class RegisterPage(BaseClass):
    
    def __init__(self, driver):
        super().__init__(driver) # self.driver = driver, this changes to super() when we introduce baseclass here
        
    first_name_id = "input-firstname"
    last_name_id = "input-lastname"
    email_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    radio_agree_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    newsletter_yes_xpath = "//input[@name='newsletter'][@value='1']"
    privacy_policy_error_xpath = "//div[@id='account-register']/div"
    first_name_error_xpath = "//fieldset[1]/div[@class='form-group required has-error'][1]/div/div"
    last_name_error_xpath = "//fieldset[1]/div[@class='form-group required has-error'][2]/div/div"
    email_error_xpath = "//fieldset[1]/div[@class='form-group required has-error'][3]/div/div"
    telephone_error_xpath = "//fieldset[1]/div[@class='form-group required has-error'][4]/div/div"
    password_error_xpath = "//fieldset[2]/div[@class='form-group required has-error']/div/div"
    
    
    def input_first_name(self, firstname):
        self.type(firstname, "first_name_id", self.first_name_id) # returning the type function of baseclass here: the 3 lines can be discarded
        # self.driver.find_element(By.ID, self.first_name_id).click()
        # self.driver.find_element(By.ID, self.first_name_id).clear()
        # self.driver.find_element(By.ID, self.first_name_id).send_keys(firstname)
        
    def input_last_name(self, lastname):
        self.type(lastname, "last_name_id", self.last_name_id) # returning the type function of baseclass here: the 3 lines can be discarded
        # self.driver.find_element(By.ID, self.last_name_id).click()
        # self.driver.find_element(By.ID, self.last_name_id).clear()
        # self.driver.find_element(By.ID, self.last_name_id).send_keys(lastname)
        
    def input_email(self, email):
        self.type(email, "email_id", self.email_id) # returning the type function of baseclass here: the 3 lines can be discarded
        # self.driver.find_element(By.ID, self.email_id).click()
        # self.driver.find_element(By.ID, self.email_id).clear()
        # self.driver.find_element(By.ID, self.email_id).send_keys(email)
        
    def input_telephone(self, phone):
        self.type(phone, "telephone_field_id", self.telephone_field_id) # returning the type function of baseclass here: the 3 lines can be discarded
        # self.driver.find_element(By.ID, self.telephone_field_id).click()
        # self.driver.find_element(By.ID, self.telephone_field_id).clear()
        # self.driver.find_element(By.ID, self.telephone_field_id).send_keys(phone)
        
    def input_password(self, password):
        self.type(password, "password_field_id", self.password_field_id) # returning the type function of baseclass here: the 3 lines can be discarded
        # self.driver.find_element(By.ID, self.password_field_id).click()
        # self.driver.find_element(By.ID, self.password_field_id).clear()
        # self.driver.find_element(By.ID, self.password_field_id).send_keys(password)
        
    def confirm_password(self, confirm_password):
        self.type(confirm_password, "confirm_password_field_id", self.confirm_password_field_id) # returning the type function of baseclass here: the 3 lines can be discarded
        # self.driver.find_element(By.ID, self.confirm_password_field_id).click()
        # self.driver.find_element(By.ID, self.confirm_password_field_id).clear()
        # self.driver.find_element(By.ID, self.confirm_password_field_id).send_keys(confirm_password)
        
        
    # this is the function that takes all the input from the parametrize(data driven)
    def input_all_values(self, firstname, lastname, email, phone, password, confirm_password):
        self.input_first_name(firstname)
        self.input_last_name(lastname)
        self.input_email(email)
        self.input_telephone(phone)
        self.input_password(password)
        self.confirm_password(confirm_password)
        
    def radio_agree_terms(self):
        self.element_click("radio_agree_name", self.radio_agree_name) #returning the "element_click" function from baseclass
        # self.driver.find_element(By.NAME, self.radio_agree_name).click()
        
    def continue_button(self):
        self.element_click("continue_button_xpath", self.continue_button_xpath) #returning the "element_click" function from baseclass
        # self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return AccountSuccess(self.driver)
        
    def agree_to_newsletter(self):
        self.element_click("newsletter_yes_xpath", self.newsletter_yes_xpath) #returning the "element_click" function from baseclass
        # self.driver.find_element(By.XPATH, self.newsletter_yes_xpath).click()
        
    def privacy_policy_error_message(self):
        return self.check_for_text("privacy_policy_error_xpath", self.privacy_policy_error_xpath)  # returning the "check_for_text" function from baseclass
        # return self.driver.find_element(By.XPATH, self.privacy_policy_error_xpath).text
    
    def input_first_name_error_message(self):
        return self.check_for_text("first_name_error_xpath", self.first_name_error_xpath)  # returning the "check_for_text" function from baseclass
        # return self.driver.find_element(By.XPATH, self.first_name_error_xpath).text
    
    def input_last_name_error_message(self):
        return self.check_for_text("last_name_error_xpath", self.last_name_error_xpath)  # returning the "check_for_text" function from baseclass
        # return self.driver.find_element(By.XPATH, self.last_name_error_xpath).text
    
    def input_email_error_message(self):
        return self.check_for_text("email_error_xpath", self.email_error_xpath)  # returning the "check_for_text" function from baseclass
        # return self.driver.find_element(By.XPATH, self.email_error_xpath).text
    
    def input_phone_error_message(self):
        return self.check_for_text("telephone_error_xpath", self.telephone_error_xpath)  # returning the "check_for_text" function from baseclass
        # return self.driver.find_element(By.XPATH, self.telephone_error_xpath).text
    
    def input_password_error_message(self):
        return self.check_for_text("password_error_xpath", self.password_error_xpath)  # returning the "check_for_text" function from baseclass
        # return self.driver.find_element(By.XPATH, self.password_error_xpath).text
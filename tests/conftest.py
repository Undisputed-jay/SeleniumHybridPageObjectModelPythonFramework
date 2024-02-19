import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import ReadConfigurations # import this after setting the configurations



@pytest.fixture()
def setup_and_teardown(request):
    # global driver # This works for all the driver
    browser = ReadConfigurations.read_configuration("basic info", "browser") # here we pass the category name and key name
    driver = None # this is to use firefox, edge and chrome browser, if i change the browser to firefox in the config.ini, browser in config can be changed to chrome or edge
    if browser.__eq__("chrome"): # to check if the browser is another browser 
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")
    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(app_url )
    request.cls.driver = driver  #this allows us to be able to use the driver for other testfiles, thereby changing the driver  to self.driver
    yield
    driver.quit()

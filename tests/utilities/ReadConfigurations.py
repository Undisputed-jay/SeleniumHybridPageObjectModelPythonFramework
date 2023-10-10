# this is for the reading from configuration

from configparser import ConfigParser

# category is basic info while key is the browser

def read_configuration(category, key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)

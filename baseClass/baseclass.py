# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from PIL import Image
from Screenshot import Screenshot_Clipping
import time 

class BaseClass:
    
    def __init__(self, driver):
        self.driver = driver
        
    def max_window(self):
        self.driver.maximize_window()    
        
    ################ action methods for locators         
    
    def find_element(self, locator):
        return self.driver.find_element_by_xpath(locator)
        
    def fill_data(self, element, data):
        element.send_keys(data)    

    def click_element(self, element):
        element.click()
    
    def get_attribute(self, element, attr):
        return element.get_attribute(attr)     
        
    def get_title(self):
        return self.driver.title
    
    def get_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])
    
    
    ################ reporting methods for locators
     
    
    def get_screenshot(self, name):
        self.driver.save_screenshot(name)
        
    def show_screenshot(self, name):
        screenshot = Image.open(name)
        screenshot.show()
    

    ################ sleep methods for locators    
    
        
    def sleep(self, duration):
        time.sleep(duration)
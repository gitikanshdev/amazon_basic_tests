from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from baseClass.baseclass import BaseClass
from selenium.webdriver.support.ui import Select


class Test_001:
    
    baseUrl = "https://www.amazon.in/"
    data = "shoes"
    result_file= "final_screenshot.png"
    

################################  Test 1 #######################################


    def test_search(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
                
        ###### create class object BaseClass
        
        self.bp = BaseClass(self.driver)
               
        self.bp.max_window()
        element = self.bp.find_element("//div[@id='nav-belt']/div/div/form/div[2]/div/input")
        self.bp.fill_data(element, "shoes")
        element = self.bp.find_element("//div[@id='nav-belt']/div/div/form/div[3]/div/span/input")
        self.bp.click_element(element)
        
        
        #### verifying result page via page title
        #### Replace "Amazon.in : " which is common in every page title
        
        title = self.bp.get_title().replace("Amazon.in : ","")
        
        if title == self.data:
            assert True
        
        else:
            assert False    
        
        
        #### verifying result page via amazon search result text
        
        element = self.bp.find_element("//span[@class='rush-component']/div/span/h1/div/div/div/div/span[3]")
        
        search_result = element.text.strip('"')
        
        if search_result == self.data:
            assert True
        
        else:
            assert False
            
            
            
################################  Test 2 #######################################    

            
        
        ##### applying filters and wait
        ## filter : get item by tomorrow        
        
        element = self.bp.find_element("//div[@class='a-section a-spacing-double-large']/div[1]/ul/li[1]/span/a/div/label/i")
        self.bp.click_element(element)
        self.bp.sleep(5)
        
        
        ## filter : get item of top customer rating
        
        element = self.bp.find_element("//div[@class='a-section a-spacing-double-large']/div[3]/ul/li[1]/span/a/section/i")
        self.bp.click_element(element)
        self.bp.sleep(5)        
        
        title = self.driver.title
        
        if title == "Amazon.in: shoes - 4 Stars & Up / Get It by Tomorrow":
            assert True
        
        else:
            assert False
            

################################  Test 3 #######################################    
    
    
        #### test on the first item
        
        element = self.bp.find_element("//img[@data-image-index='1']")   
        first_item_name = self.bp.get_attribute(element, "alt")
        self.bp.click_element(element)
        
        ### Moving to another window
        
        self.bp.get_new_window()
        
        new_page_item = self.bp.find_element("//span[@id='productTitle']")
        new_page_item_name = new_page_item.text
        
        #### check product details

        if first_item_name == new_page_item_name:
            assert True
        
        else:
            assert False
            

        select = Select(self.bp.find_element('//select[@name="dropdown_selected_size_name"]'))
        select.select_by_index(1)
        self.bp.sleep(5)

        element = self.bp.find_element("//input[@id='add-to-cart-button']")
        self.bp.click_element(element)


        #### take screenshot of the result page

        self.bp.get_screenshot(self.result_file)
        self.bp.show_screenshot(self.result_file)
            
            
        self.driver.close()            
        
        
        
        
        
        

        
    
    


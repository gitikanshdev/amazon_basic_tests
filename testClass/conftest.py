from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest 

#### decorator

@pytest.fixture
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver
    
    
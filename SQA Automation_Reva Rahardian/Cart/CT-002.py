import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_delete_products_in_cart(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/cart.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[4]/a").click()
        time.sleep(2)

        response_message = browser.find_element(By.ID,"totalp").text

        self.assertNotIn('820', response_message)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
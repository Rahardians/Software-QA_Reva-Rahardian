import unittest
import time
import random
import string
from selenium import webdriver 
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_register_username_morethan_16_Characters(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("rvrahardian1777")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("revarahardianpurwokerto123")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'password must be between 3 and 20 characters')

        Alert(browser).accept()

        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
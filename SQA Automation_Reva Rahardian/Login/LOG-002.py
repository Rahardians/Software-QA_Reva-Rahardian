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

    def test_a_login_with_wrong_username(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"login2").click()
        time.sleep(1)
        browser.find_element(By.ID,"loginusername").send_keys("rvrahardians12")
        time.sleep(1)
        browser.find_element(By.ID,"loginpassword").send_keys("purwokerto")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'User does not exist.')

        Alert(browser).accept()

        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
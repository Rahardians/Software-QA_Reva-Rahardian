import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_send_message(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/nav/div[1]/ul/li[2]/a").click()
        time.sleep(1)
        browser.find_element(By.ID,"recipient-email").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"recipient-name").send_keys("Reva Rahardian")
        time.sleep(1)
        browser.find_element(By.ID,"message-text").send_keys("Congratulations!!!")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/button[2]").click()
        time.sleep(2)
        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Thanks for the message!!')


        Alert(browser).accept()

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
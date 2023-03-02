import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_add_variative_products_to_cart(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/nav/div/div/ul/li[1]/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[4]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/nav/div/div/ul/li[1]/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[6]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)

        response_message = browser.find_element(By.ID,"totalp").text

        self.assertEqual(response_message, '2400')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
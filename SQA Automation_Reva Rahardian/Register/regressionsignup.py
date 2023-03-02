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

    
    def test_a_register(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(1)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("rvrahardian")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("rvrahardian")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)
        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Sign up successful.')

        Alert(browser).accept()

    def test_a_register_with_already_username(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("rvrahardian")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("rvrahardian")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'This user already exist.')

        Alert(browser).accept()

    def test_a_register_username_contain_symbols(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("rvrahardian%")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("rahardians")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Username cannot contain symbols.')

        Alert(browser).accept()

    def test_a_register_password_contain_symbol(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("rvrahardian177")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("rvrahardian%")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Username cannot contain symbols.')

        Alert(browser).accept()

    def test_a_register_empty_username(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("rahardians")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Username and Password.')

        Alert(browser).accept()

    def test_a_failed_register_with_empty_password(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("rahardians")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Username and Password.')

        Alert(browser).accept()

    def test_a_register_empty_username_password(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Username and Password.')

        Alert(browser).accept()

    def test_a_register_username_less_8_Characters(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("pyt")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("rvrahardian")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Username must contain at least 8 characters')

        Alert(browser).accept()

    def test_a_register_username_less_8_Characters(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("rvrahardian1177")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("pyt")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Password must contain at least 8 characters')

        Alert(browser).accept()

    def test_a_register_username_morethan_16_Characters(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("revarahardianpurwokerto123")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("rvrahardian")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'username must be between 3 and 20 characters')

        Alert(browser).accept()

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

    def test_a_register_same_username_and_password(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("rvrahardian")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("rvrahardian")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'password must be between 3 and 20 characters')

        Alert(browser).accept()

    def test_a_register_capitalize_username(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("RAJAWALI")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("rvrahardian")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Username must not capitalize')

        Alert(browser).accept()

    def test_a_register_capitalize_password(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("guitar")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("GUITARIST")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Password must not capitalize')

        Alert(browser).accept()

        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
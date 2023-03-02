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

    def test_a_success_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("03")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')
    
    def test_a_cancel_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[1]").click()
        time.sleep(2)

    def test_a_order_with_empty_name_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"country").send_keys("Indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Name and Creditcard.')

        Alert(browser).accept()
    
    def test_a_order_with_empty_country_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Country')

        Alert(browser).accept()

    def test_a_order_with_empty_city_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("Indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out city')

        Alert(browser).accept()

    def test_a_failed_order_with_empty_creditcard_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("Indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Name and Creditcard.')

        Alert(browser).accept()
    
    def test_a_failed_order_with_empty_month_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("Indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Name and Creditcard.')

        Alert(browser).accept()
    
    def test_a_failed_order_with_empty_year_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("Indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Name and Creditcard.')

        Alert(browser).accept()
    
    def test_a_failed_order_with_empty_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Name and Creditcard.')

        Alert(browser).accept()
    
    def test_a_creditcard_contain_letter_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910PQW")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("03")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')
    
    def test_a_credicard_contain_symbol_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910%$")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("Juli")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')
    
    def test_a_month_contain_letter_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("Juli")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')
    
    def test_a_month_contain_symbol_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07&")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')
    
    def test_a_year_contain_letter_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023Sekarang")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')
    
    def test_a_year_contain_symbol_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023*")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')
    
    def test_a_name_contain_number_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva176")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')
    
    def test_a_name_contain_symbol_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva&")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')
    
    
    def test_a_country_contain_number(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia62")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')
    
    def test_a_country_contain_symbol_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva176")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("@indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')
    
    def test_a_city_contain_number_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva176")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("@indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("Banyumas12")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')

    def test_a_city_contain_symbol_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("Reva176")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("@indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("@Banyumas")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("12345678910")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("07")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2023")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')
        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
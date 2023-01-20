import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pytest import PytestAssertRewriteWarning

class testUpdateUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_TCU_1(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"Username").send_keys("admin123")
        driver.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        driver.find_element(By.NAME,"login").click()
        time.sleep(2)
        driver.find_element(By.ID,"searching").send_keys("Nichole")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        driver.find_element(By.XPATH,"/html/body/div//table//a[@href='/Customer/Edit/3771']").click()
        driver.find_element(By.ID,"Name").clear()
        time.sleep(2)
        driver.find_element(By.ID,"Name").send_keys("Nichole Kidman")
        driver.find_element(By.XPATH,"/html/body/div/form[@action='/Customer/Edit/3771']//input[@value='Save']").click()
        time.sleep(2)
        driver.find_element(By.ID,"searching").send_keys("Nichole Kidman")
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        time.sleep(5)

        response_message = driver.find_element(By.XPATH,"/html/body/div//h1[.='Dashboard']").text
        self.assertEqual(response_message,"Dashboard")

    def test_TCU_2(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"Username").send_keys("admin123")
        driver.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        driver.find_element(By.NAME,"login").click()
        time.sleep(2)
        driver.find_element(By.ID,"searching").send_keys("Dalila")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        driver.find_element(By.XPATH,"/html/body/div//table//a[@href='/Customer/Edit/3787']").click()
        time.sleep(3)
        driver.find_element(By.ID,"Email").clear()
        driver.find_element(By.ID,"Email").send_keys("LilianThuram@baringung.com")
        driver.find_element(By.XPATH,"/html/body/div/form[@action='/Customer/Edit/3787']//input[@value='Save']").click()
        driver.find_element(By.ID,"searching").send_keys("Dalila")
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        time.sleep(5)

        response_message = driver.find_element(By.XPATH,"/html/body/div//h1[.='Dashboard']").text
        self.assertEqual(response_message,"Dashboard")

    def test_TCU_3(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"Username").send_keys("admin123")
        driver.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        driver.find_element(By.NAME,"login").click()
        time.sleep(2)
        driver.find_element(By.ID,"searching").send_keys("Elísio")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        driver.find_element(By.XPATH,"/html/body/div//table//a[@href='/Customer/Edit/3783']").click()
        time.sleep(3)
        driver.find_element(By.ID,"Address").clear()
        driver.find_element(By.ID,"Address").send_keys("jalan jalan sore keliling")
        driver.find_element(By.XPATH,"/html/body/div/form[@action='/Customer/Edit/3783']//input[@value='Save']").click()
        driver.find_element(By.ID,"searching").send_keys("Elísio")
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        time.sleep(5)

        response_message = driver.find_element(By.XPATH,"/html/body/div//h1[.='Dashboard']").text
        self.assertEqual(response_message,"Dashboard")

    def test_TCU_4(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"Username").send_keys("admin123")
        driver.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        driver.find_element(By.NAME,"login").click()
        time.sleep(2)
        driver.find_element(By.ID,"searching").send_keys("Fabrícia")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        driver.find_element(By.XPATH,"/html/body/div//table//a[@href='/Customer/Edit/3798']").click()
        time.sleep(3)
        driver.find_element(By.ID,"Phone").clear()
        driver.find_element(By.ID,"Phone").send_keys("085623412666")
        driver.find_element(By.XPATH,"/html/body/div/form[@action='/Customer/Edit/3798']//input[@value='Save']").click()
        driver.find_element(By.ID,"searching").send_keys("Fabrícia")
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        time.sleep(5)

        response_message = driver.find_element(By.XPATH,"/html/body/div//h1[.='Dashboard']").text
        self.assertEqual(response_message,"Dashboard")

    def tearDown(self): 
        self.browser.close()

unittest.main()
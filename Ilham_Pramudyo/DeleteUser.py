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
        driver.find_element(By.ID,"searching").send_keys("Miss Rupert Cartwright")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        driver.find_element(By.XPATH,"/html/body/div//table//a[@href='/Customer/Delete/3825']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div//form[@action='/Customer/Delete/3825']//input[@value='Delete']").click()
        driver.find_element(By.ID,"searching").send_keys("Miss Rupert Cartwright")
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        time.sleep(5)

        response_message = driver.find_element(By.XPATH,"/html/body/div//h1[.='Dashboard']").text
        self.assertEqual(response_message,"Dashboard")

    def tearDown(self): 
        self.browser.close()

unittest.main()
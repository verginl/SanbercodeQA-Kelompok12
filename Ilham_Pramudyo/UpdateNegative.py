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
        driver.find_element(By.ID,"searching").send_keys("Angelena Moore")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        driver.find_element(By.XPATH,"/html/body/div//table//a[@href='/Customer/Edit/3789']").click()
        driver.find_element(By.ID,"Name").clear()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div/form[@action='/Customer/Edit/3789']//input[@value='Save']").click()
        time.sleep(2)
        driver.find_element(By.ID,"searching").send_keys("geraldine.abshire@hotmail.com")
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        time.sleep(5)

        response_message = driver.find_element(By.XPATH,"/html/body/div//h1[.='Dashboard']").text
        self.assertEqual(response_message,"Dashboard")

    def est_TCU_2(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"Username").send_keys("admin123")
        driver.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        driver.find_element(By.NAME,"login").click()
        time.sleep(2)
        driver.find_element(By.ID,"searching").send_keys("Frederico da Gam")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        driver.find_element(By.XPATH,"/html/body/div//table//a[@href='/Customer/Edit/3763']").click()
        time.sleep(3)
        driver.find_element(By.ID,"Email").clear()
        driver.find_element(By.XPATH,"/html/body/div/form[@action='/Customer/Edit/3763']//input[@value='Save']").click()
        driver.find_element(By.ID,"searching").send_keys("Frederico da Gam")
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        time.sleep(5)

        response_message = driver.find_element(By.XPATH,"/html/body/div//h1[.='Dashboard']").text
        self.assertEqual(response_message,"Dashboard")

    def est_TCU_3(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"Username").send_keys("admin123")
        driver.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        driver.find_element(By.NAME,"login").click()
        time.sleep(2)
        driver.find_element(By.ID,"searching").send_keys("Hélio Rios")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        driver.find_element(By.XPATH,"/html/body/div//table//a[@href='/Customer/Edit/3781']").click()
        time.sleep(3)
        driver.find_element(By.ID,"Phone").clear()
        driver.find_element(By.XPATH,"/html/body/div/form[@action='/Customer/Edit/3781']//input[@value='Save']").click()
        driver.find_element(By.ID,"searching").send_keys("Hélio Rios")
        driver.find_element(By.XPATH,"/html//form[@action='/Dashboard']/input[@value='Search']").click()
        time.sleep(5)

        response_message = driver.find_element(By.XPATH,"/html/body/div//h1[.='Dashboard']").text
        self.assertEqual(response_message,"Dashboard")


    def tearDown(self): 
        self.browser.close()

unittest.main()
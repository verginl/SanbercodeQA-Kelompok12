import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Basic(unittest.TestCase):
    def setUp(self):
         options = webdriver.ChromeOptions()
         options.add_experimental_option('excludeSwitches', ['enable-logging'])
         self.driver = webdriver.Chrome(options=options)
         self.driver.maximize_window()
         self.driver.get('https://itera-qa.azurewebsites.net/') #Buka Situs       

    # def test_login_success(self):
    #     driver = self.driver       
    #     BtnLogin = self.driver.find_element(By.XPATH, '//*[@id="navbarColor01"]/form/ul/li[2]/a')
    #     BtnLogin.click()
    #     TxtUsername = driver.find_element(by=By.ID, value='Username')
    #     TxtUsername.send_keys("admin123")
       
    #     TxtPassword = driver.find_element(by=By.ID, value='Password')
    #     TxtPassword.send_keys('1234')
       
    #     BtnLogin = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]')
    #     BtnLogin.click()
    #     time.sleep(3)

    #     actualRslt = "Dashboard"
    #     response_message = driver.find_element(By.XPATH,"/html/body/div/div/h1").text
    #     self.assertEqual(response_message, actualRslt)

    # def test_login_success_uppercase(self):
    #     driver = self.driver       
    #     BtnLogin = self.driver.find_element(By.XPATH, '//*[@id="navbarColor01"]/form/ul/li[2]/a')
    #     BtnLogin.click()
    #     TxtUsername = driver.find_element(by=By.ID, value='Username')
    #     TxtUsername.send_keys("ADMIN123")
       
    #     TxtPassword = driver.find_element(by=By.ID, value='Password')
    #     TxtPassword.send_keys('1234')
       
    #     BtnLogin = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]')
    #     BtnLogin.click()
    #     time.sleep(3)

    #     actualRslt = "Dashboard"
    #     response_message = driver.find_element(By.XPATH,"/html/body/div/div/h1").text
    #     self.assertEqual(response_message, actualRslt)

    # def test_login_fail_wrongpassword(self):
    #     driver = self.driver       
    #     BtnLogin = self.driver.find_element(By.XPATH, '//*[@id="navbarColor01"]/form/ul/li[2]/a')
    #     BtnLogin.click()
    #     TxtUsername = driver.find_element(by=By.ID, value='Username')
    #     TxtUsername.send_keys("admin123")
       
    #     TxtPassword = driver.find_element(by=By.ID, value='Password')
    #     TxtPassword.send_keys('alif123')
       
    #     BtnLogin = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]')
    #     BtnLogin.click()
    #     time.sleep(3)

    #     actualRslt = driver.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[5]/td/label").text
    #     expectRslt = "Wrong username or password"
    #     self.assertEqual(actualRslt,expectRslt)

    # def test_login_fail_wrongusername(self):
    #     driver = self.driver       
    #     BtnLogin = self.driver.find_element(By.XPATH, '//*[@id="navbarColor01"]/form/ul/li[2]/a')
    #     BtnLogin.click()
    #     TxtUsername = driver.find_element(by=By.ID, value='Username')
    #     TxtUsername.send_keys("intan")
       
    #     TxtPassword = driver.find_element(by=By.ID, value='Password')
    #     TxtPassword.send_keys('1234')
       
    #     BtnLogin = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]')
    #     BtnLogin.click()
    #     time.sleep(3)

    #     actualRslt = driver.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[5]/td/label").text
    #     expectRslt = "Wrong username or password"
    #     self.assertEqual(actualRslt,expectRslt)


    # def test_login_fail_blank(self):
    #     driver = self.driver       
    #     BtnLogin = self.driver.find_element(By.XPATH, '//*[@id="navbarColor01"]/form/ul/li[2]/a')
    #     BtnLogin.click()
       
    #     BtnLogin = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]')
    #     BtnLogin.click()
    #     time.sleep(3)

    #     actualRslt = driver.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[3]/td/span").text
    #     expectRslt = "Please enter username"
    #     self.assertEqual(actualRslt,expectRslt)

    #     actualRslt2 = driver.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[5]/td/label").text
    #     expectRslt2 = "Wrong username or password"
    #     self.assertEqual(actualRslt2,expectRslt2)

    #     actualRslt3 = driver.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[6]/td/span").text
    #     expectRslt3 = "Please enter password"
    #     self.assertEqual(actualRslt3,expectRslt3)

    # def test_login_fail_blankusername(self):
    #     driver = self.driver       
    #     BtnLogin = self.driver.find_element(By.XPATH, '//*[@id="navbarColor01"]/form/ul/li[2]/a')
    #     BtnLogin.click()
       
    #     TxtPassword = driver.find_element(by=By.ID, value='Password')
    #     TxtPassword.send_keys('1234')
       
    #     BtnLogin = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]')
    #     BtnLogin.click()
    #     time.sleep(3)

    #     actualRslt = driver.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[5]/td/label").text
    #     expectRslt = "Wrong username or password"
    #     self.assertEqual(actualRslt,expectRslt)

    # def test_login_fail_blankpassword(self):
    #     driver = self.driver       
    #     BtnLogin = self.driver.find_element(By.XPATH, '//*[@id="navbarColor01"]/form/ul/li[2]/a')
    #     BtnLogin.click()
    #     TxtUsername = driver.find_element(by=By.ID, value='Username')
    #     TxtUsername.send_keys("admin123")
       
    #     BtnLogin = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]')
    #     BtnLogin.click()
    #     time.sleep(3)

    #     actualRslt = driver.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[5]/td/label").text
    #     expectRslt = "Wrong username or password"
    #     self.assertEqual(actualRslt,expectRslt)

    # def test_login_button_Not_Registered(self):
    #     driver = self.driver       
    #     BtnLogin = self.driver.find_element(By.XPATH, '//*[@id="navbarColor01"]/form/ul/li[2]/a')
    #     BtnLogin.click()

    #     BtnNotRegistered = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/table/tbody/tr[8]/td/a')
    #     BtnNotRegistered.click()
    #     time.sleep(3)

    #     actualRslt = "Add new user"
    #     response_message = driver.find_element(By.XPATH,"/html/body/div/h2").text
    #     self.assertEqual(response_message, actualRslt)

    # def test_login_button_clear(self):
    #     driver = self.driver       
    #     BtnLogin = driver.find_element(By.XPATH, '//*[@id="navbarColor01"]/form/ul/li[2]/a')
    #     BtnLogin.click()

    #     TxtUsername = driver.find_element(by=By.ID, value='Username')
    #     TxtUsername.send_keys("admin123")
       
    #     TxtPassword = driver.find_element(by=By.ID, value='Password')
    #     TxtPassword.send_keys('1234')

    #     BtnClear = driver.find_element(By.XPATH, '//html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[2]')
    #     BtnClear.click()
    #     time.sleep(3)

    #     txtUsername = driver.find_element(By.ID,"Username").text
    #     txtPassword = driver.find_element(By.ID,"Password").text
    #     assert txtUsername == "" and txtPassword ==""

    def test_logout_success(self):
        driver = self.driver       
        BtnLogin = self.driver.find_element(By.XPATH, '//*[@id="navbarColor01"]/form/ul/li[2]/a')
        BtnLogin.click()
        TxtUsername = driver.find_element(by=By.ID, value='Username')
        TxtUsername.send_keys("admin123")
       
        TxtPassword = driver.find_element(by=By.ID, value='Password')
        TxtPassword.send_keys('1234')
       
        BtnLogin = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]')
        BtnLogin.click()
        time.sleep(3)

        BtnLogout = driver.find_element(By.XPATH, '//*[@id="navbarColor01"]/form/ul/li[2]/a')
        BtnLogout.click()
        time.sleep(3)

        actualRslt = driver.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[1]/td[2]").text
        expectRslt = "LOGIN"
        self.assertEqual(actualRslt,expectRslt)
      

unittest.main()




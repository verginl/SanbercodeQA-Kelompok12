import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class test(unittest.TestCase):

    def setUp(self):
        self.webdash = webdriver.Chrome(ChromeDriverManager().install())

    def test1_dashboard_screen(self):
        webdash = self.webdash
        webdash.get("https://itera-qa.azurewebsites.net/Login")
        webdash.maximize_window()
        time.sleep(1)
        webdash.find_element(By.ID,"Username").send_keys("admin123") 
        time.sleep(1)
        webdash.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        webdash.find_element(By.NAME,"login").click()
        time.sleep(3)
        get_url = webdash.current_url
        self.assertEqual(get_url, "https://itera-qa.azurewebsites.net/Dashboard")

    def test2_button_createnew(self):
        webdash = self.webdash
        webdash.get("https://itera-qa.azurewebsites.net/Login")
        webdash.maximize_window()
        time.sleep(1)
        webdash.find_element(By.ID,"Username").send_keys("admin123") 
        time.sleep(1)
        webdash.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        webdash.find_element(By.NAME,"login").click()
        time.sleep(1)
        webdash.find_element(By.CSS_SELECTOR,"a.btn.btn-primary").click()
        time.sleep(3)
        get_url = webdash.current_url
        self.assertEqual(get_url, "https://itera-qa.azurewebsites.net/Customer/Create")

    def test3_button_search(self):
        webdash = self.webdash
        webdash.get("https://itera-qa.azurewebsites.net/Login")
        webdash.maximize_window()
        time.sleep(1)
        webdash.find_element(By.ID,"Username").send_keys("admin123") 
        time.sleep(1)
        webdash.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        webdash.find_element(By.NAME,"login").click()
        time.sleep(1)
        webdash.find_element(By.ID,"searching").send_keys("babar")
        time.sleep(1)
        webdash.find_element(By.CSS_SELECTOR,"input.btn.btn-secondary.my-2.my-sm-0").click()
        time.sleep(3)
        get_url = webdash.current_url
        self.assertEqual(get_url, "https://itera-qa.azurewebsites.net/Dashboard?searching=babar")
    
    def test4_button_search_negative(self):
        webdash = self.webdash    
        webdash.get("https://itera-qa.azurewebsites.net/Login")
        webdash.maximize_window()
        time.sleep(1)
        webdash.find_element(By.ID,"Username").send_keys("admin123") 
        time.sleep(1)
        webdash.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        webdash.find_element(By.NAME,"login").click()
        time.sleep(1)
        webdash.find_element(By.ID,"searching").send_keys("")
        time.sleep(1)
        webdash.find_element(By.CSS_SELECTOR,"input.btn.btn-secondary.my-2.my-sm-0").click()
        time.sleep(3)
        get_url = webdash.current_url
        self.assertEqual(get_url, "https://itera-qa.azurewebsites.net/Dashboard?searching=")

    def test5_button_searchblank_negative(self):
        webdash = self.webdash    
        webdash.get("https://itera-qa.azurewebsites.net/Login")
        webdash.maximize_window()
        time.sleep(1)
        webdash.find_element(By.ID,"Username").send_keys("admin123") 
        time.sleep(1)
        webdash.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        webdash.find_element(By.NAME,"login").click()
        time.sleep(1)
        webdash.find_element(By.ID,"searching").send_keys("dfasdfasdfa")
        time.sleep(1)
        webdash.find_element(By.CSS_SELECTOR,"input.btn.btn-secondary.my-2.my-sm-0").click()
        time.sleep(3)
        header_page = webdash.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[2]/td").text
        self.assertEqual(header_page, "No Match")

    def test6_button_edit(self):
        webdash = self.webdash    
        webdash.get("https://itera-qa.azurewebsites.net/Login")
        webdash.maximize_window()
        time.sleep(1)
        webdash.find_element(By.ID,"Username").send_keys("admin123") 
        time.sleep(1)
        webdash.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        webdash.find_element(By.NAME,"login").click()
        time.sleep(1)
        webdash.find_element(By.CSS_SELECTOR,"a.btn.btn-outline-primary").click()
        time.sleep(3)
        header_page = webdash.find_element(By.XPATH,"/html/body/div/h2").text
        self.assertEqual(header_page, "Edit")
        
    def test7_button_details(self):
        webdash = self.webdash    
        webdash.get("https://itera-qa.azurewebsites.net/Login")
        webdash.maximize_window()
        time.sleep(1)
        webdash.find_element(By.ID,"Username").send_keys("admin123") 
        time.sleep(1)
        webdash.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        webdash.find_element(By.NAME,"login").click()
        time.sleep(1)
        webdash.find_element(By.CSS_SELECTOR,"a.btn.btn-outline-info").click()
        time.sleep(3)
        header_page = webdash.find_element(By.XPATH,"/html/body/div/h2").text
        self.assertEqual(header_page, "Details")

    def test8_button_edit(self):
        webdash = self.webdash    
        webdash.get("https://itera-qa.azurewebsites.net/Login")
        webdash.maximize_window()
        time.sleep(1)
        webdash.find_element(By.ID,"Username").send_keys("admin123") 
        time.sleep(1)
        webdash.find_element(By.ID,"Password").send_keys("1234")
        time.sleep(1)
        webdash.find_element(By.NAME,"login").click()
        time.sleep(1)
        webdash.find_element(By.CSS_SELECTOR,"a.btn.btn-outline-danger").click()
        time.sleep(3)
        header_page = webdash.find_element(By.XPATH,"/html/body/div/h2").text
        self.assertEqual(header_page, "Delete")

unittest.main()
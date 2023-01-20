from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest import mark
from _pytest.mark.structures import Mark
import pytest
import time

#================================ WEB BROWSER CHROME ==================================#

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])    
@pytest.fixture
def setUp():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://itera-qa.azurewebsites.net/")
    driver.implicitly_wait(10)
    yield driver
    driver.maximize_window()
    driver.quit()

#======================================================================================#

#============================ TEST CASE CREATE ============================#

@pytest.mark.test01_login_standartcorrect
def test01_create_standartcorrect(setUp):
     #Login as pre-condition
     textlogin = setUp.find_element(By.XPATH,"//a[contains(text(),'Login')]")
     textlogin.click()
     txtname = setUp.find_element(By.NAME,"Username")
     txtname.send_keys("admin123")
     txtpass = setUp.find_element(By.NAME,"Password")
     txtpass.send_keys("1234")
     btnlogin = setUp.find_element(By.XPATH,"//tbody/tr[7]/td[2]/input[1]")
     btnlogin.click()
     time.sleep(5)

    #create as pre-condition (standart correct - positive case)  
     btnCreate = setUp.find_element(By.XPATH,"//a[contains(text(),'Create New')]")
     btnCreate.click()
     time.sleep(2)
     txtName = setUp.find_element(By.XPATH,"//input[@id='Name']")
     txtName.send_keys("ustin bieber")
     time.sleep(2)
     txtCompany = setUp.find_element(By.XPATH,"//input[@id='Company']")
     txtCompany.send_keys("France")
     time.sleep(2)
     txtAdress = setUp.find_element(By.XPATH,"//input[@id='Address']")
     txtAdress.send_keys("st kingston 116")
     time.sleep(2)
     txtCity = setUp.find_element(By.XPATH,"//input[@id='City']")
     txtCity.send_keys("paris")
     time.sleep(2)
     txtPhone = setUp.find_element(By.XPATH,"//input[@id='Phone']")
     txtPhone.send_keys("117817")
     time.sleep(2)
     txtMail = setUp.find_element(By.XPATH,"//input[@id='Email']")
     txtMail.send_keys("jb@mail.com")
     time.sleep(2)
     btnCreate = setUp.find_element(By.XPATH,"//body/div[1]/form[1]/div[1]/div[7]/div[1]/input[1]")
     btnCreate.click()
     time.sleep(5)

     #Validation After Create Data
     Validation = setUp.find_element(By.XPATH,("//h1[contains(text(),'Dashboard')]"))
     assert Validation
     time.sleep(5)

@pytest.mark.test02_login_capitalalphabet
def test02_create_capitalalphabet(setUp):
     #Login as pre-condition
     textlogin = setUp.find_element(By.XPATH,"//a[contains(text(),'Login')]")
     textlogin.click()
     txtname = setUp.find_element(By.NAME,"Username")
     txtname.send_keys("admin123")
     txtpass = setUp.find_element(By.NAME,"Password")
     txtpass.send_keys("1234")
     btnlogin = setUp.find_element(By.XPATH,"//tbody/tr[7]/td[2]/input[1]")
     btnlogin.click()
     time.sleep(5)

    #create as pre-condition (capital alphabet - positve case) 
     btnCreate = setUp.find_element(By.XPATH,"//a[contains(text(),'Create New')]")
     btnCreate.click()
     time.sleep(2)
     txtName = setUp.find_element(By.XPATH,"//input[@id='Name']")
     txtName.send_keys("BTS ARMY")
     time.sleep(2)
     txtCompany = setUp.find_element(By.XPATH,"//input[@id='Company']")
     txtCompany.send_keys("BIGHITEND")
     time.sleep(2)
     txtAdress = setUp.find_element(By.XPATH,"//input[@id='Address']")
     txtAdress.send_keys("KOREA CABANG DEPOK")
     time.sleep(2)
     txtCity = setUp.find_element(By.XPATH,"//input[@id='City']")
     txtCity.send_keys("DEPOK")
     time.sleep(2)
     txtPhone = setUp.find_element(By.XPATH,"//input[@id='Phone']")
     txtPhone.send_keys("9117")
     time.sleep(2)
     txtMail = setUp.find_element(By.XPATH,"//input[@id='Email']")
     txtMail.send_keys("BTSARMY@MAIL.COM")
     time.sleep(2)
     btnCreate = setUp.find_element(By.XPATH,"//body/div[1]/form[1]/div[1]/div[7]/div[1]/input[1]")
     btnCreate.click()
     time.sleep(5)

     #Validation After Create Data
     Validation = setUp.find_element(By.XPATH,("//h1[contains(text(),'Dashboard')]"))
     assert Validation
     time.sleep(5)

@pytest.mark.test03_login_inputadressfieldonly
def test03_create_inputadressfieldonly(setUp):
     #Login as pre-condition
     textlogin = setUp.find_element(By.XPATH,"//a[contains(text(),'Login')]")
     textlogin.click()
     txtname = setUp.find_element(By.NAME,"Username")
     txtname.send_keys("admin123")
     txtpass = setUp.find_element(By.NAME,"Password")
     txtpass.send_keys("1234")
     btnlogin = setUp.find_element(By.XPATH,"//tbody/tr[7]/td[2]/input[1]")
     btnlogin.click()
     time.sleep(5)

     #create as pre-condition ( inputadressfieldonly - negative case) 
     btnCreate = setUp.find_element(By.XPATH,"//a[contains(text(),'Create New')]")
     btnCreate.click()
     time.sleep(2)
     txtName = setUp.find_element(By.XPATH,"//input[@id='Name']")
     txtName.send_keys("")
     time.sleep(2)
     txtCompany = setUp.find_element(By.XPATH,"//input[@id='Company']")
     txtCompany.send_keys("")
     time.sleep(2)
     txtAdress = setUp.find_element(By.XPATH,"//input[@id='Address']")
     txtAdress.send_keys("<3")
     time.sleep(2)
     txtCity = setUp.find_element(By.XPATH,"//input[@id='City']")
     txtCity.send_keys("")
     time.sleep(2)
     txtPhone = setUp.find_element(By.XPATH,"//input[@id='Phone']")
     txtPhone.send_keys("")
     time.sleep(2)
     txtMail = setUp.find_element(By.XPATH,"//input[@id='Email']")
     txtMail.send_keys("")
     time.sleep(2)
     btnCreate = setUp.find_element(By.XPATH,"//body/div[1]/form[1]/div[1]/div[7]/div[1]/input[1]")
     btnCreate.click()
     time.sleep(5)

     #Validation After Create Data
     Validation = setUp.find_element(By.XPATH,("//h1[contains(text(),'Dashboard')]"))
     assert Validation
     time.sleep(5)

@pytest.mark.test04_login_blankfield
def test04_create_blankfield(setUp):
     #Login as pre-condition
     textlogin = setUp.find_element(By.XPATH,"//a[contains(text(),'Login')]")
     textlogin.click()
     txtname = setUp.find_element(By.NAME,"Username")
     txtname.send_keys("admin123")
     txtpass = setUp.find_element(By.NAME,"Password")
     txtpass.send_keys("1234")
     btnlogin = setUp.find_element(By.XPATH,"//tbody/tr[7]/td[2]/input[1]")
     btnlogin.click()
     time.sleep(5)

     #create as pre-condition ( blankfield - negative case) 
     btnCreate = setUp.find_element(By.XPATH,"//a[contains(text(),'Create New')]")
     btnCreate.click()
     time.sleep(2)
     txtName = setUp.find_element(By.XPATH,"//input[@id='Name']")
     txtName.send_keys("")
     time.sleep(2)
     txtCompany = setUp.find_element(By.XPATH,"//input[@id='Company']")
     txtCompany.send_keys("")
     time.sleep(2)
     txtAdress = setUp.find_element(By.XPATH,"//input[@id='Address']")
     txtAdress.send_keys("")
     time.sleep(2)
     txtCity = setUp.find_element(By.XPATH,"//input[@id='City']")
     txtCity.send_keys("")
     time.sleep(2)
     txtPhone = setUp.find_element(By.XPATH,"//input[@id='Phone']")
     txtPhone.send_keys("")
     time.sleep(2)
     txtMail = setUp.find_element(By.XPATH,"//input[@id='Email']")
     txtMail.send_keys("")
     time.sleep(2)
     btnCreate = setUp.find_element(By.XPATH,"//body/div[1]/form[1]/div[1]/div[7]/div[1]/input[1]")
     btnCreate.click()
     time.sleep(5)

     #Validation After Create Data
     Validation = setUp.find_element(By.XPATH,("//h1[contains(text(),'Dashboard')]"))
     assert Validation
     time.sleep(5)

@pytest.mark.test05_login_backtolist
def test04_create_backtolist(setUp):
     #Login as pre-condition
     textlogin = setUp.find_element(By.XPATH,"//a[contains(text(),'Login')]")
     textlogin.click()
     txtname = setUp.find_element(By.NAME,"Username")
     txtname.send_keys("admin123")
     txtpass = setUp.find_element(By.NAME,"Password")
     txtpass.send_keys("1234")
     btnlogin = setUp.find_element(By.XPATH,"//tbody/tr[7]/td[2]/input[1]")
     btnlogin.click()
     time.sleep(5)

     #create as pre-condition ( blankfield - negative case) 
     btnCreate = setUp.find_element(By.XPATH,"//a[contains(text(),'Create New')]")
     btnCreate.click()
     time.sleep(2)
     txtName = setUp.find_element(By.XPATH,"//input[@id='Name']")
     txtName.send_keys("")
     time.sleep(2)
     txtCompany = setUp.find_element(By.XPATH,"//input[@id='Company']")
     txtCompany.send_keys("")
     time.sleep(2)
     txtAdress = setUp.find_element(By.XPATH,"//input[@id='Address']")
     txtAdress.send_keys("")
     time.sleep(2)
     txtCity = setUp.find_element(By.XPATH,"//input[@id='City']")
     txtCity.send_keys("")
     time.sleep(2)
     txtPhone = setUp.find_element(By.XPATH,"//input[@id='Phone']")
     txtPhone.send_keys("")
     time.sleep(2)
     txtMail = setUp.find_element(By.XPATH,"//input[@id='Email']")
     txtMail.send_keys("")
     time.sleep(2)

     #Back To List
     txtBacktolist = setUp.find_element(By.XPATH,"//a[contains(text(),'Back to List')]")
     txtBacktolist.click()
     time.sleep(5)

     #Validation After Create Data
     Validation = setUp.find_element(By.XPATH,("//h1[contains(text(),'Dashboard')]"))
     assert Validation
     time.sleep(5)

#======================================================================================#

#============================ TEST CASE READ ============================#

@pytest.mark.test06_read_searchbyname
def test06_read_searchbyname(setUp):
     #Login as pre-condition
     textlogin = setUp.find_element(By.XPATH,"//a[contains(text(),'Login')]")
     textlogin.click()
     txtname = setUp.find_element(By.NAME,"Username")
     txtname.send_keys("admin123")
     txtpass = setUp.find_element(By.NAME,"Password")
     txtpass.send_keys("1234")
     btnlogin = setUp.find_element(By.XPATH,"//tbody/tr[7]/td[2]/input[1]")
     btnlogin.click()
     time.sleep(5)

     #create as pre-condition ( Search by Name - Positive case) 
     searchName = setUp.find_element(By.XPATH,"//input[@id='searching']")
     searchName.send_keys("justin")
     time.sleep(2)
     btnSearch = setUp.find_element(By.XPATH,"//body/div[1]/div[1]/form[1]/input[2]")
     btnSearch.click()

@pytest.mark.test07_read_searchbyemail
def test07_read_searchbyemail(setUp):
     #Login as pre-condition
     textlogin = setUp.find_element(By.XPATH,"//a[contains(text(),'Login')]")
     textlogin.click()
     txtname = setUp.find_element(By.NAME,"Username")
     txtname.send_keys("admin123")
     txtpass = setUp.find_element(By.NAME,"Password")
     txtpass.send_keys("1234")
     btnlogin = setUp.find_element(By.XPATH,"//tbody/tr[7]/td[2]/input[1]")
     btnlogin.click()
     time.sleep(5)

     #create as pre-condition ( Search by Name - Positive case) 
     searchEmail = setUp.find_element(By.XPATH,"//input[@id='searching']")
     searchEmail.send_keys("jb@mail.com")
     time.sleep(2)
     btnSearch = setUp.find_element(By.XPATH,"//body/div[1]/div[1]/form[1]/input[2]")
     btnSearch.click()

@pytest.mark.test08_read_readdetail
def test08_read_readdetail(setUp):
     #Login as pre-condition
     textlogin = setUp.find_element(By.XPATH,"//a[contains(text(),'Login')]")
     textlogin.click()
     txtname = setUp.find_element(By.NAME,"Username")
     txtname.send_keys("admin123")
     txtpass = setUp.find_element(By.NAME,"Password")
     txtpass.send_keys("1234")
     btnlogin = setUp.find_element(By.XPATH,"//tbody/tr[7]/td[2]/input[1]")
     btnlogin.click()
     time.sleep(5)

     #create as pre-condition ( Read Detail - Positive case) 
     searchName = setUp.find_element(By.XPATH,"//input[@id='searching']")
     searchName.send_keys("BTS ARMY")
     time.sleep(2)
     btnSearch = setUp.find_element(By.XPATH,"//body/div[1]/div[1]/form[1]/input[2]")
     btnSearch.click()
     btnDetails = setUp.find_element(By.XPATH,"//tbody/tr[2]/td[7]/a[2]")
     btnDetails.click()

@pytest.mark.test09_read_backtolist
def test09_read_backtolist(setUp):
     #Login as pre-condition
     textlogin = setUp.find_element(By.XPATH,"//a[contains(text(),'Login')]")
     textlogin.click()
     txtname = setUp.find_element(By.NAME,"Username")
     txtname.send_keys("admin123")
     txtpass = setUp.find_element(By.NAME,"Password")
     txtpass.send_keys("1234")
     btnlogin = setUp.find_element(By.XPATH,"//tbody/tr[7]/td[2]/input[1]")
     btnlogin.click()
     time.sleep(5)

     #create as pre-condition ( Read Detail - Positive case) 
     searchName = setUp.find_element(By.XPATH,"//input[@id='searching']")
     searchName.send_keys("BTS ARMY")
     time.sleep(2)
     btnSearch = setUp.find_element(By.XPATH,"//body/div[1]/div[1]/form[1]/input[2]")
     btnSearch.click()
     time.sleep(2)
     btnDetails = setUp.find_element(By.XPATH,"//tbody/tr[2]/td[7]/a[2]")
     btnDetails.click()
     time.sleep(5)

    #Back To List
     txtbacktolist = setUp.find_element(By.XPATH,"//a[contains(text(),'Back to List')]")
     txtbacktolist.click()
     time.sleep(5)

@pytest.mark.test10_read_searchbyphone
def test10_read_searchbyphone(setUp):
     #Login as pre-condition
     textlogin = setUp.find_element(By.XPATH,"//a[contains(text(),'Login')]")
     textlogin.click()
     txtname = setUp.find_element(By.NAME,"Username")
     txtname.send_keys("admin123")
     txtpass = setUp.find_element(By.NAME,"Password")
     txtpass.send_keys("1234")
     btnlogin = setUp.find_element(By.XPATH,"//tbody/tr[7]/td[2]/input[1]")
     btnlogin.click()
     time.sleep(5)

     #create as pre-condition ( Search by Phone - Negative case) 
     searchName = setUp.find_element(By.XPATH,"//input[@id='searching']")
     searchName.send_keys("117817")
     time.sleep(2)
     btnSearch = setUp.find_element(By.XPATH,"//body/div[1]/div[1]/form[1]/input[2]")
     btnSearch.click()
     time.sleep(2)

@pytest.mark.test10_read_searchbycompany
def test10_read_searchbycompany(setUp):
     #Login as pre-condition
     textlogin = setUp.find_element(By.XPATH,"//a[contains(text(),'Login')]")
     textlogin.click()
     txtname = setUp.find_element(By.NAME,"Username")
     txtname.send_keys("admin123")
     txtpass = setUp.find_element(By.NAME,"Password")
     txtpass.send_keys("1234")
     btnlogin = setUp.find_element(By.XPATH,"//tbody/tr[7]/td[2]/input[1]")
     btnlogin.click()
     time.sleep(5)

     #create as pre-condition ( Search by Company - Negative case) 
     searchName = setUp.find_element(By.XPATH,"//input[@id='searching']")
     searchName.send_keys("France")
     time.sleep(2)
     btnSearch = setUp.find_element(By.XPATH,"//body/div[1]/div[1]/form[1]/input[2]")
     btnSearch.click()
     time.sleep(2)

@pytest.mark.test11_read_searchbyadress
def test11_read_searchbyadress(setUp):
     #Login as pre-condition
     textlogin = setUp.find_element(By.XPATH,"//a[contains(text(),'Login')]")
     textlogin.click()
     txtname = setUp.find_element(By.NAME,"Username")
     txtname.send_keys("admin123")
     txtpass = setUp.find_element(By.NAME,"Password")
     txtpass.send_keys("1234")
     btnlogin = setUp.find_element(By.XPATH,"//tbody/tr[7]/td[2]/input[1]")
     btnlogin.click()
     time.sleep(5)

     #create as pre-condition ( Search by Adress - Negative case )
     searchName = setUp.find_element(By.XPATH,"//input[@id='searching']")
     searchName.send_keys("st kingston 116")
     time.sleep(2)
     btnSearch = setUp.find_element(By.XPATH,"//body/div[1]/div[1]/form[1]/input[2]")
     btnSearch.click()
     time.sleep(2)

@pytest.mark.test12_read_searchbycity
def test11_read_searchbycity(setUp):
     #Login as pre-condition
     textlogin = setUp.find_element(By.XPATH,"//a[contains(text(),'Login')]")
     textlogin.click()
     txtname = setUp.find_element(By.NAME,"Username")
     txtname.send_keys("admin123")
     txtpass = setUp.find_element(By.NAME,"Password")
     txtpass.send_keys("1234")
     btnlogin = setUp.find_element(By.XPATH,"//tbody/tr[7]/td[2]/input[1]")
     btnlogin.click()
     time.sleep(5)

     #create as pre-condition ( Search by Adress - Negative case )
     searchName = setUp.find_element(By.XPATH,"//input[@id='searching']")
     searchName.send_keys("paris")
     time.sleep(2)
     btnSearch = setUp.find_element(By.XPATH,"//body/div[1]/div[1]/form[1]/input[2]")
     btnSearch.click()
     time.sleep(2)



#=================================================================================#  

        

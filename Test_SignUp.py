from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest import mark
from _pytest.mark.structures import Mark
import pytest
import time
from BaseScript import BaseScript

# CATATAN : UNTUK RUN FILE INI BISA KETIK : Pytest Test_SignUp.py -v

#================================ WEB BROWSER FIREFOX ==================================#
# options = webdriver.FirefoxOptions()
# @pytest.fixture
# def setUp():
#     driver = webdriver.Firefox(options=options)
#     driver.maximize_window()
#     driver.get("https://itera-qa.azurewebsites.net/")
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#======================================================================================#

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
    driver.quit()
#======================================================================================#
#============================= TEST CASE SIGN UP SUCCESS ==============================#
@pytest.mark.signUpSuccess_TC_001
def test_signUpSuccess_TC_001(setUp): #TC_001 Success Login
    btnsignUp = setUp.find_element(By.XPATH, "//*[@id='navbarColor01']/form/ul/li[1]/a")
    btnsignUp.click()

    txtSurename = setUp.find_element(By.ID, "FirstName")
    txtSurename.send_keys(BaseScript.randomInputStr(10))

    txtSurename = setUp.find_element(By.ID, "Surname")
    txtSurename.send_keys(BaseScript.randomInputStr(20))

    txtEPost = setUp.find_element(By.ID, "E_post")
    txtEPost.send_keys(BaseScript.randomInputNumb(5))

    txtMobile = setUp.find_element(By.ID, "Mobile")
    txtMobile.send_keys(BaseScript.randomInputNumb(12))

    txtUsername = setUp.find_element(By.ID, "Username")
    txtUsername.send_keys(BaseScript.randomInputStr(10))

    txtPassword = setUp.find_element(By.ID, "Password")
    txtPassword.send_keys("Password123")

    txtPassword = setUp.find_element(By.ID, "ConfirmPassword")
    txtPassword.send_keys("Password123")

    btnSubmit = setUp.find_element(By.ID, "submit")
    setUp.execute_script("arguments[0].click();", btnSubmit)
    
    time.sleep(3)

    Response = setUp.find_element(By.XPATH,"/html/body/div/form/div/div[9]/div/label").text
    assert Response == "Registration Successful"

@pytest.mark.signUpSuccess_TC_002
def test_signUpSuccess_TC_002_EmptyEpost(setUp): #TC_002 Success Login Empty E Post
    btnsignUp = setUp.find_element(By.XPATH, "//*[@id='navbarColor01']/form/ul/li[1]/a")
    btnsignUp.click()

    txtSurename = setUp.find_element(By.ID, "FirstName")
    txtSurename.send_keys(BaseScript.randomInputStr(10))

    txtSurename = setUp.find_element(By.ID, "Surname")
    txtSurename.send_keys(BaseScript.randomInputStr(20))

    txtMobile = setUp.find_element(By.ID, "Mobile")
    txtMobile.send_keys(BaseScript.randomInputNumb(12))

    txtUsername = setUp.find_element(By.ID, "Username")
    txtUsername.send_keys(BaseScript.randomInputStr(10))

    txtPassword = setUp.find_element(By.ID, "Password")
    txtPassword.send_keys("Password123")

    txtPassword = setUp.find_element(By.ID, "ConfirmPassword")
    txtPassword.send_keys("Password123")

    btnSubmit = setUp.find_element(By.ID, "submit")
    setUp.execute_script("arguments[0].click();", btnSubmit)
    
    time.sleep(3)

    Response = setUp.find_element(By.XPATH,"/html/body/div/form/div/div[9]/div/label").text
    assert Response == "Registration Successful"

@pytest.mark.signUpSuccess_TC_003
def test_signUpSuccess_TC_003EmptyMobile(setUp): #TC_003 Success Login Empty Mobile
    btnsignUp = setUp.find_element(By.XPATH, "//*[@id='navbarColor01']/form/ul/li[1]/a")
    btnsignUp.click()

    txtSurename = setUp.find_element(By.ID, "FirstName")
    txtSurename.send_keys(BaseScript.randomInputStr(10))

    txtSurename = setUp.find_element(By.ID, "Surname")
    txtSurename.send_keys(BaseScript.randomInputStr(20))

    txtEPost = setUp.find_element(By.ID, "E_post")
    txtEPost.send_keys(BaseScript.randomInputNumb(5))

    txtUsername = setUp.find_element(By.ID, "Username")
    txtUsername.send_keys(BaseScript.randomInputStr(10))

    txtPassword = setUp.find_element(By.ID, "Password")
    txtPassword.send_keys("Password123")

    txtPassword = setUp.find_element(By.ID, "ConfirmPassword")
    txtPassword.send_keys("Password123")

    btnSubmit = setUp.find_element(By.ID, "submit")
    setUp.execute_script("arguments[0].click();", btnSubmit)
    
    time.sleep(3)

    Response = setUp.find_element(By.XPATH,"/html/body/div/form/div/div[9]/div/label").text
    assert Response == "Registration Successful"
#=================================================================================#

#============================ TEST CASE SIGN UP FAIL ============================#
@pytest.mark.signUpFail_TC_004
def test_signUpFail_TC_004_BlankField(setUp): #TC_004 Blank Field
    btnsignUp = setUp.find_element(By.XPATH, "//*[@id='navbarColor01']/form/ul/li[1]/a")
    btnsignUp.click()

    btnSubmit = setUp.find_element(By.ID, "submit")
    setUp.execute_script("arguments[0].click();", btnSubmit)

    Response1 = setUp.find_element(By.ID,"FirstName-error").text
    Response2 = setUp.find_element(By.ID,"Surname-error").text
    Response3 = setUp.find_element(By.ID,"Username-error").text
    Response4 = setUp.find_element(By.ID,"Password-error").text
    assert Response1 == "Please enter first name" and Response2 == "Please enter surname" and Response3 == "Please enter username" and Response4 == "Please enter password"
  
@pytest.mark.signUpFail_TC_005
def test_signUpFail_TC_005_EmptyFirstName(setUp): #TC_005 Empty First Name
    btnsignUp = setUp.find_element(By.XPATH, "//*[@id='navbarColor01']/form/ul/li[1]/a")
    btnsignUp.click()

    txtSurename = setUp.find_element(By.ID, "Surname")
    txtSurename.send_keys("Nardian Lufyandi")

    txtEPost = setUp.find_element(By.ID, "E_post")
    txtEPost.send_keys("16722")

    txtMobile = setUp.find_element(By.ID, "Mobile")
    txtMobile.send_keys("081380008744")

    txtUsername = setUp.find_element(By.ID, "Username")
    txtUsername.send_keys("verginardian4")

    txtPassword = setUp.find_element(By.ID, "Password")
    txtPassword.send_keys("Verginl123")

    txtConfirmPassword = setUp.find_element(By.ID, "ConfirmPassword")
    txtConfirmPassword.send_keys("Verginl123")

    btnSubmit = setUp.find_element(By.ID, "submit")
    setUp.execute_script("arguments[0].click();", btnSubmit)
    
    time.sleep(3)

    Response = setUp.find_element(By.ID,"FirstName-error").text
    assert Response == "Please enter first name"

@pytest.mark.signUpFail_TC_006
def test_signUpFail_TC_006_EmptySurname(setUp): #TC_006 Empty Surname
    btnsignUp = setUp.find_element(By.XPATH, "//*[@id='navbarColor01']/form/ul/li[1]/a")
    btnsignUp.click()

    txtSurename = setUp.find_element(By.ID, "FirstName")
    txtSurename.send_keys("Vergi")

    txtEPost = setUp.find_element(By.ID, "E_post")
    txtEPost.send_keys("16722")

    txtMobile = setUp.find_element(By.ID, "Mobile")
    txtMobile.send_keys("081380008744")

    txtUsername = setUp.find_element(By.ID, "Username")
    txtUsername.send_keys("verginardian4")

    txtPassword = setUp.find_element(By.ID, "Password")
    txtPassword.send_keys("Verginl123")

    txtConfirmPassword = setUp.find_element(By.ID, "ConfirmPassword")
    txtConfirmPassword.send_keys("Verginl123")

    btnSubmit = setUp.find_element(By.ID, "submit")
    setUp.execute_script("arguments[0].click();", btnSubmit)
    
    time.sleep(3)

    Response = setUp.find_element(By.ID,"Surname-error").text
    assert Response == "Please enter surname"

@pytest.mark.signUpFail_TC_007
def test_signUpFail_TC_007_EmptyUsername(setUp): #TC_007 Empty Username
    btnsignUp = setUp.find_element(By.XPATH, "//*[@id='navbarColor01']/form/ul/li[1]/a")
    btnsignUp.click()

    txtSurename = setUp.find_element(By.ID, "FirstName")
    txtSurename.send_keys("Vergi")

    txtSurename = setUp.find_element(By.ID, "Surname")
    txtSurename.send_keys("Nardian Lufyandi")

    txtEPost = setUp.find_element(By.ID, "E_post")
    txtEPost.send_keys("16722")

    txtMobile = setUp.find_element(By.ID, "Mobile")
    txtMobile.send_keys("081380008744")

    txtPassword = setUp.find_element(By.ID, "Password")
    txtPassword.send_keys("Verginl123")

    txtConfirmPassword = setUp.find_element(By.ID, "ConfirmPassword")
    txtConfirmPassword.send_keys("Verginl123")

    btnSubmit = setUp.find_element(By.ID, "submit")
    setUp.execute_script("arguments[0].click();", btnSubmit)
    
    time.sleep(3)

    Response = setUp.find_element(By.ID,"Username-error").text
    assert Response == "Please enter username"

@pytest.mark.signUpFail_TC_008
def test_signUpFail_TC_008_EmptyPassword(setUp): #TC_008 Empty Password
    btnsignUp = setUp.find_element(By.XPATH, "//*[@id='navbarColor01']/form/ul/li[1]/a")
    btnsignUp.click()

    txtSurename = setUp.find_element(By.ID, "FirstName")
    txtSurename.send_keys("Vergi")

    txtSurename = setUp.find_element(By.ID, "Surname")
    txtSurename.send_keys("Nardian Lufyandi")

    txtEPost = setUp.find_element(By.ID, "E_post")
    txtEPost.send_keys("16722")

    txtMobile = setUp.find_element(By.ID, "Mobile")
    txtMobile.send_keys("081380008744")

    txtUsername = setUp.find_element(By.ID, "Username")
    txtUsername.send_keys("verginardian4")

    txtConfirmPassword = setUp.find_element(By.ID, "ConfirmPassword")
    txtConfirmPassword.send_keys("Verginl123")

    btnSubmit = setUp.find_element(By.ID, "submit")
    setUp.execute_script("arguments[0].click();", btnSubmit)
    
    time.sleep(3)

    Response1 = setUp.find_element(By.ID,"Password-error").text
    Response2 = setUp.find_element(By.ID,"ConfirmPassword-error").text
    assert Response1 == "Please enter password" and Response2 == "'Confirm password' and 'Password' do not match."

@pytest.mark.signUpFail_TC_009
def test_signUpFail_TC_009_EmptyConfirmPassword(setUp): #TC_009 Empty Confirm Password
    btnsignUp = setUp.find_element(By.XPATH, "//*[@id='navbarColor01']/form/ul/li[1]/a")
    btnsignUp.click()

    txtSurename = setUp.find_element(By.ID, "FirstName")
    txtSurename.send_keys("Vergi")

    txtSurename = setUp.find_element(By.ID, "Surname")
    txtSurename.send_keys("Nardian Lufyandi")

    txtEPost = setUp.find_element(By.ID, "E_post")
    txtEPost.send_keys("16722")

    txtMobile = setUp.find_element(By.ID, "Mobile")
    txtMobile.send_keys("081380008744")

    txtUsername = setUp.find_element(By.ID, "Username")
    txtUsername.send_keys("verginardian4")

    txtPassword = setUp.find_element(By.ID, "Password")
    txtPassword.send_keys("Verginl123")

    btnSubmit = setUp.find_element(By.ID, "submit")
    setUp.execute_script("arguments[0].click();", btnSubmit)
    
    time.sleep(3)

    Response = setUp.find_element(By.ID,"ConfirmPassword-error").text
    assert Response == "'Confirm password' and 'Password' do not match."

@pytest.mark.signUpFail_TC_010
def test_signUpFail_TC_010_WrongConfirmPassword(setUp): #TC_010 Wrong Confirm Password
    btnsignUp = setUp.find_element(By.XPATH, "//*[@id='navbarColor01']/form/ul/li[1]/a")
    btnsignUp.click()

    txtSurename = setUp.find_element(By.ID, "FirstName")
    txtSurename.send_keys("Vergi")

    txtSurename = setUp.find_element(By.ID, "Surname")
    txtSurename.send_keys("Nardian Lufyandi")

    txtEPost = setUp.find_element(By.ID, "E_post")
    txtEPost.send_keys("16722")

    txtMobile = setUp.find_element(By.ID, "Mobile")
    txtMobile.send_keys("081380008744")

    txtUsername = setUp.find_element(By.ID, "Username")
    txtUsername.send_keys("verginardian4")

    txtPassword = setUp.find_element(By.ID, "Password")
    txtPassword.send_keys("Verginl123")

    txtPassword = setUp.find_element(By.ID, "ConfirmPassword")
    txtPassword.send_keys("salah123")

    btnSubmit = setUp.find_element(By.ID, "submit")
    setUp.execute_script("arguments[0].click();", btnSubmit)
    
    time.sleep(3)

    Response = setUp.find_element(By.ID,"ConfirmPassword-error").text
    assert Response == "'Confirm password' and 'Password' do not match."

@pytest.mark.signUpFail_TC_011
def test_signUpFail_TC_011_UsernameAlreadyExist(setUp): #TC_011 Username Already Exist
    btnsignUp = setUp.find_element(By.XPATH, "//*[@id='navbarColor01']/form/ul/li[1]/a")
    btnsignUp.click()

    txtSurename = setUp.find_element(By.ID, "FirstName")
    txtSurename.send_keys("Vergi")

    txtSurename = setUp.find_element(By.ID, "Surname")
    txtSurename.send_keys("Nardian Lufyandi")

    txtEPost = setUp.find_element(By.ID, "E_post")
    txtEPost.send_keys("16722")

    txtMobile = setUp.find_element(By.ID, "Mobile")
    txtMobile.send_keys("081380008744")

    txtUsername = setUp.find_element(By.ID, "Username")
    txtUsername.send_keys("verginardian")

    txtPassword = setUp.find_element(By.ID, "Password")
    txtPassword.send_keys("Verginl123")

    txtPassword = setUp.find_element(By.ID, "ConfirmPassword")
    txtPassword.send_keys("Verginl123")

    btnSubmit = setUp.find_element(By.ID, "submit")
    setUp.execute_script("arguments[0].click();", btnSubmit)
    
    time.sleep(3)

    Response = setUp.find_element(By.XPATH,"/html/body/div/form/div/div[10]/div/label").text
    assert Response == "Username already exist"

#=================================================================================#  




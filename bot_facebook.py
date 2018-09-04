from selenium import webdriver
username='pruebas.gtdaniel@gmail.com'
password='C124321C124321'

url= 'https://www.fb.com/'

driver=webdriver.Chrome("C:\webdrivers\chromedriver.exe")
driver.get(url)
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()
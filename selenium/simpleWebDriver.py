from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys

driver = webdriver.Chrome("C:\\Python37-32\\Scripts\\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
title = driver.title
print(title)
print(sys.platform)


assert "Welcome: Mercury Tours" in title

driver.find_element_by_link_text("REGISTER").click()
try:
    driver.implicitly_wait(10)
    driver.find_element_by_name("firstName").send_keys("Test")
    driver.find_element_by_name("lastName").send_keys("Testy")
    driver.find_element_by_name("email").send_keys("test@test.com")
    driver.find_element_by_name("password").send_keys("Test123")
    driver.find_element_by_name("confirmPassword").send_keys("Test123")


    select = Select(driver.find_element_by_name("country"))
    for option in select.options:
        #print(option.text)
        if option.text == 'INDIA ':
            print ("----------------------------------------------------------------------")
            option.click()

    time.sleep(10)

    driver.find_element_by_name("register").click()

    url = driver.current_url
    print(url)
    assert "http://newtours.demoaut.com/create_account_success.php" in url

    driver.find_element(By.LINK_TEXT, 'Flights').click()

    elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//input[2]')))

    driver.find_element(By.XPATH,'//input[2]').click()
    select = Select(driver.find_element(By.XPATH,'//*[@name="passCount"]'))
    select.select_by_value("2")
    driver.implicitly_wait(10)

    select = Select(driver.find_element(By.XPATH,'//*[@name="fromPort"]'))
    select.select_by_index("4")
    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, '//*[@name="servClass"]').click()
    select = Select(driver.find_element(By.XPATH, '//*[@name="airline"]'))
    select.select_by_visible_text("Blue Skies Airlines")

    driver.find_element_by_name("findFlights").click()

finally:
    print ("Success")
    #driver.quit()

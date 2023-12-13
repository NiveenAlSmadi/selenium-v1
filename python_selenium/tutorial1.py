from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome()

driver.get("https://app.chalktalk.com/login")

email=driver.find_element(By.NAME, "email")
password=driver.find_element(By.NAME, "password")
accept= driver.find_element(By.LINK_TEXT, 'Accept')
accept.click()
email.send_keys("qa@2023.com")
password.send_keys(12345678)
password.send_keys(Keys.RETURN)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "app"))
    )
except:
    driver.quit()   
time.sleep(5)

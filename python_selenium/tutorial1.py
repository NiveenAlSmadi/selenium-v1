from selenium import webdriver
driver=webdriver.Chrome()

driver.get("https://app.chalktalk.com/login")
driver.close()
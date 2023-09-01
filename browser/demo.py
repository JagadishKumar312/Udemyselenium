from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()  # Service Manager
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")

print(driver.current_url)
print(driver.title)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.refresh()
driver.back()
driver.close()

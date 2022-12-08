from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver = webdriver.Chrome()
webdriver.get('https://www.booking.com')
# site_rezervari = webdriver.find_element(By.CSS_SELECTOR, 'form[method="GET"] button[type="submit"]')
# site_rezervari.click()
sleep(50)
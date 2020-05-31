
from selenium import webdriver
from time import sleep

browser_driver = webdriver.Firefox(executable_path='C:/Users/hasan/Documents/Python/week6-python-selenium-task-AikaHasanova/geckodriver')
browser_driver.get('http://35.225.243.133/admin/login/')
browser_driver.find_element_by_name('username').send_keys('student')
browser_driver.find_element_by_id('id_password').send_keys('qatester')
browser_driver.find_element_by_css_selector('#login-form > div.submit-row > input[type=submit]').click()
sleep(5)
browser_driver.find_element_by_css_selector('#content-main > div > table > tbody > tr.model-blog > td:nth-child(2) > a').click()
sleep(5)
browser_driver.find_element_by_css_selector('#container > div.breadcrumbs > a:nth-child(1)').click()
sleep(3)
browser_driver.find_element_by_css_selector('#content-main > div > table > tbody > tr.model-blogger > td:nth-child(2) > a:nth-child(1)').click()

browser_driver.find_element_by_name('full_name').send_keys('AikaHasanova')
sleep(3)

browser_driver.find_element_by_css_selector('#blogger_form > div > div > input.default').click()
sleep(5)

browser_driver.close()

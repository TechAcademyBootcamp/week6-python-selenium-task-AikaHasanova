from selenium import webdriver

browser_driver = webdriver.Firefox(executable_path='C:/Users/hasan/Documents/Python/week6-python-selenium-task-AikaHasanova/geckodriver')
browser_driver.get('https://www.facebook.com/')
browser_driver.find_element_by_name('email').send_keys('')
browser_driver.find_element_by_id('pass').send_keys('')
browser_driver.find_element_by_css_selector('#loginbutton').click()

browser_driver.close()
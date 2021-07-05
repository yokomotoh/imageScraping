import time

from selenium import webdriver


driver = webdriver.Chrome('/Users/vincent/Desktop/Scraping/chromedriver')  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');
###  sample test
###  https://sites.google.com/chromium.org/driver/getting-started?authuser=0
'''
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
'''
###
time.sleep(5)
search_box = driver.find_element_by_css_selector('input.gLFyf')
search_box.send_keys('Dog')
time.sleep(5)
driver.quit()
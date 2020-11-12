from selenium import webdriver as wd
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.remote.webelement import WebElement
from keys import get_keys, get_urls


CHROME_DRIVER_PATH = get_keys()['chromedriver']

options = ChromeOptions()
options.add_argument('--headless')

driver = Chrome(CHROME_DRIVER_PATH, options=options)

driver.get(get_urls()['triennale'])

driver.find_element_by_xpath('//*[@id="accordion371"]/div[2]/div[1]/span[2]/a').click()
print(driver.find_element_by_xpath('//*[@id="collapseInternoX1"]/table/tbody/tr[2]/td[2]').text)
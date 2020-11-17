from selenium import webdriver as wd
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from keys import get_keys, get_urls
from time import sleep

CHROME_DRIVER_PATH = get_keys()['chromedriver']

options = ChromeOptions()
options.add_argument('--headless')
driver = Chrome(CHROME_DRIVER_PATH, options=options)
wait = WebDriverWait(driver, 5)

def scrape(tables):
    for table in tables:
        length = len(table.find_elements_by_xpath('tr'))
        for i in range(2, length+1):
            try:
                if ',' in table.find_element_by_xpath(f'tr[{i}]/td[4]').text:
                    print(table.find_element_by_xpath(f'tr[{i}]/td[2]').text + ',"' + table.find_element_by_xpath(f'tr[{i}]/td[4]').text + '"')
                else:
                    print(table.find_element_by_xpath(f'tr[{i}]/td[2]').text + ',' + table.find_element_by_xpath(f'tr[{i}]/td[4]').text)
            except:
                continue
            
def tables_triennale():
    driver.get(get_urls()['triennale'])
    driver.find_element_by_id('expandAllId').click()
    sleep(2)
    tables = []
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/div[2]/div/div[2]/table/tbody'))
    tables.append(driver.find_element_by_xpath('//*[@id="collapseInternoX8"]/table/tbody'))
    tables.append(driver.find_element_by_xpath('//*[@id="collapseInternoX8"]/table/tbody'))
    tables.append(driver.find_element_by_xpath('//*[@id="collapseInternoX17"]/table/tbody'))
    tables.append(driver.find_element_by_xpath('//*[@id="collapseInternofiglio19999223404168007"]/table/tbody'))
    tables.append(driver.find_element_by_xpath('//*[@id="collapseInternonipote19999223404168007"]/table/tbody'))
    tables.append(driver.find_element_by_xpath('//*[@id="collapseInternonipote19999223404167999"]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/div[4]/div[2]/div/div[2]/table/tbody'))
    return tables

def tables_bachelor():
    driver.get(get_urls()['bachelor'])
    driver.find_element_by_id('expandAllId').click()
    sleep(2)
    tables = []
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/main/div/div/div/div[3]/div[2]/div[2]/div/div[2]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/main/div/div/div/div[3]/div[2]/div[2]/div/div[3]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/main/div/div/div/div[3]/div[2]/div[2]/div/div[4]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/main/div/div/div/div[3]/div[2]/div[2]/div/div[6]/table/tbody'))
    return tables

def tables_magistrale():
    driver.get(get_urls()['magistrale'])
    driver.find_element_by_id('expandAllId').click()
    sleep(2)
    tables = []
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/div[2]/div/font/div[1]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/div[2]/div/font/div[2]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/div[2]/div/font/div[4]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/div[2]/div/font/div[8]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/div[2]/div/font/div[10]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/div[2]/div/font/div[1]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/div[2]/div/font/div[2]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/div[2]/div/font/div[4]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/div[2]/div/font/div[8]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[1]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[2]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[4]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[6]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[10]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[1]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[2]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[4]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[8]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[1]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[2]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[4]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[6]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[10]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[1]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[2]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[4]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[6]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[10]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[1]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[2]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[4]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[6]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[10]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[1]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[2]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[4]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/font/div[8]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/div[2]/table/tbody'))
    tables.append(driver.find_element_by_xpath('/html/body/div[7]/font/main/div/div/div/div[3]/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/font/div[2]/div[2]/div/div[3]/table/tbody'))
    return tables


if __name__ == '__main__':
    scrape(tables_magistrale())
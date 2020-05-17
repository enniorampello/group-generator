import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException


# load the default profile in order not to login every time
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/Users/enniorampello/Library/Application Support/Google/Chrome')

# get the chromedriver and open Telegram already logged in
driver = webdriver.Chrome(executable_path='/Users/enniorampello/venv/chromedriver', options=options)
driver.get('https://web.telegram.org/')

# default object to wait until an element becomes clickable
wait = WebDriverWait(driver, timeout=30)

time.sleep(4)

# open the file containing in each line the name of a group
file = open('/Users/enniorampello/GroupGenerator/group_names.txt', 'r')
lines = file.readlines()

# iterate through all the group names and create the corresponding Telegram groups
for line in lines:

    name = line.split(',')[0]
    code = line.split(',')[1]
    # selecting the createGroup() button and click it
    hamburger_button_xpath = '//*[@id="ng-app"]/body/div[1]/div[1]/div/div/div[1]/div/a'
    try:
        wait.until(ec.element_to_be_clickable((By.XPATH,hamburger_button_xpath))).click()
    except ElementClickInterceptedException:
        popup_xpath = '//*[@id="ng-app"]/body/div[7]/div[2]/div/div'
        wait.until(ec.invisibility_of_element((By.XPATH, popup_xpath)))
        wait.until(ec.element_to_be_clickable((By.XPATH, hamburger_button_xpath))).click()

    new_group_xpath = '//*[@id="ng-app"]/body/div[1]/div[1]/div/div/div[1]/div/ul/li[1]/a'
    wait.until(ec.element_to_be_clickable((By.XPATH,new_group_xpath))).click()


    # select riccardo cuccu to create a group and click on create
    search_tab_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[2]/div[1]/input'
    wait.until(ec.presence_of_element_located((By.XPATH,search_tab_xpath))).send_keys('riccardo cuccu')

    riccardo_cuccu_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[2]/div[2]/div/div[1]/ul/li/a/div[2]'
    wait.until(ec.element_to_be_clickable((By.XPATH,riccardo_cuccu_xpath))).click()

    create_group_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[3]/div/button[2]'
    wait.until(ec.element_to_be_clickable((By.XPATH,create_group_xpath))).click()

    time.sleep(1)
    # write the name of the group and create it
    group_name_tab_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[1]/form/div/input'
    wait.until(ec.presence_of_element_located((By.XPATH,group_name_tab_xpath))).send_keys(name)

    confirm_create_group_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[2]/button[2]'
    wait.until(ec.element_to_be_clickable((By.XPATH,confirm_create_group_xpath))).click()

    time.sleep(1)
    # add comment...
    group_header_xpath = '//*[@id="ng-app"]/body/div[1]/div[1]/div/div/div[2]/div/div[2]/a/div'
    popup_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div'
    try:
        wait.until(ec.element_to_be_clickable((By.XPATH, group_header_xpath))).click()
    except ElementClickInterceptedException:
        time.sleep(1)
        wait.until(ec.invisibility_of_element((By.XPATH, popup_xpath)))
        wait.until(ec.element_to_be_clickable((By.XPATH, group_header_xpath))).click()

    upgrade_supergroup_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[3]/div[1]/div[5]/div/a'
    wait.until(ec.element_to_be_clickable((By.XPATH, upgrade_supergroup_xpath))).click()

    confirm_upgrade_xpath = '//*[@id="ng-app"]/body/div[7]/div[2]/div/div/div[2]/button[2]/span'
    wait.until(ec.element_to_be_clickable((By.XPATH, confirm_upgrade_xpath))).click()


    group_upgraded_message = '//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/' \
                             'div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/span/span/span'
    wait.until(ec.presence_of_element_located((By.XPATH, group_upgraded_message))).click()
    try:
        wait.until(ec.element_to_be_clickable((By.XPATH, group_header_xpath))).click()
    except ElementClickInterceptedException:
        wait.until(ec.invisibility_of_element((By.XPATH, popup_xpath)))
        wait.until(ec.element_to_be_clickable((By.XPATH, group_header_xpath))).click()


    modify_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[1]/div[1]/div[1]/a[2]'
    wait.until(ec.element_to_be_clickable((By.XPATH, modify_xpath))).click()

    description_tab_xpath = '//*[@id="ng-app"]/body/div[7]/div[2]/div/div/div[1]/form/div[2]/input'
    time.sleep(1)
    wait.until(ec.presence_of_element_located((By.XPATH, description_tab_xpath))).send_keys(f'Group of the course: {name}; Code: {code};')

    save_modification_xpath = '//*[@id="ng-app"]/body/div[7]/div[2]/div/div/div[2]/button[2]'
    wait.until(ec.element_to_be_clickable((By.XPATH, save_modification_xpath))).click()

file.close()
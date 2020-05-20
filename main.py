import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException

# personal constants depending on the pc
CHROME_PROFILE_PATH = '--user-data-dir=/Users/enniorampello/Library/Application Support/Google/Chrome'
CHROME_DRIVER_PATH = '/Users/enniorampello/venv/chromedriver'
TEXT_FILE_PATH = '/Users/enniorampello/GroupGenerator/group_names.txt'

# xpaths of the various buttons to click and text tabs
hamburger_button_xpath = '//*[@id="ng-app"]/body/div[1]/div[1]/div/div/div[1]/div/a'
popup_xpath = '//*[@id="ng-app"]/body/div[7]/div[2]/div/div'
new_group_xpath = '//*[@id="ng-app"]/body/div[1]/div[1]/div/div/div[1]/div/ul/li[1]/a'
search_tab_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[2]/div[1]/input'
riccardo_cuccu_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[2]/div[2]/div/div[1]/ul/li/a/div[2]'
create_group_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[3]/div/button[2]'
group_name_tab_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[1]/form/div/input'
confirm_create_group_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[2]/button[2]'
group_header_xpath = '//*[@id="ng-app"]/body/div[1]/div[1]/div/div/div[2]/div/div[2]/a/div'
upgrade_supergroup_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[3]/div[1]/div[5]/div/a'
confirm_upgrade_xpath = '//*[@id="ng-app"]/body/div[7]/div[2]/div/div/div[2]/button[2]/span'
group_upgraded_message = '//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/span/span/span'
modify_xpath = '//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[1]/div[1]/div[1]/a[2]'
description_tab_xpath = '//*[@id="ng-app"]/body/div[7]/div[2]/div/div/div[1]/form/div[2]/input'
save_modification_xpath = '//*[@id="ng-app"]/body/div[7]/div[2]/div/div/div[2]/button[2]'

# the two main function to click a button and to write in a tab
def click(xpath):
    wait.until(ec.element_to_be_clickable((By.XPATH, xpath))).click()

def write(xpath: str, text: str):
    wait.until(ec.presence_of_element_located((By.XPATH, xpath))).send_keys(text)


# load the default profile in order not to login every time
options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)

# get the chromedriver and open Telegram already logged in
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)
driver.get('https://web.telegram.org/')

# default object to wait until an element becomes clickable
wait = WebDriverWait(driver, timeout=30)

time.sleep(4)

# open the file containing in each line the name of a group
file = open(TEXT_FILE_PATH, 'r')
lines = file.readlines()

# iterate through all the group names and create the corresponding Telegram groups
for line in lines:

    name = line.split(',')[0]
    code = line.split(',')[1]
    # selecting the createGroup() button and click it
    try:
        click(hamburger_button_xpath)
    except ElementClickInterceptedException:
        wait.until(ec.invisibility_of_element((By.XPATH, popup_xpath)))
        click(hamburger_button_xpath)

    click(new_group_xpath)

    # select riccardo cuccu to create a group and click on create
    write(search_tab_xpath,'riccardo cuccu')
    click(riccardo_cuccu_xpath)
    click(create_group_xpath)

    time.sleep(1)
    # write the name of the group and create it
    write(group_name_tab_xpath,name)
    click(confirm_create_group_xpath)

    time.sleep(1)
    # if trying to click the group header an exception occurs, it means that the popup had a delay of its closure
    # so we wait until it is not visible anymore to click again the group header
    try:
        click(group_header_xpath)
    except ElementClickInterceptedException:
        time.sleep(1)
        wait.until(ec.invisibility_of_element((By.XPATH, popup_xpath)))
        click(group_header_xpath)

    click(upgrade_supergroup_xpath)
    click(confirm_upgrade_xpath)

    # this block waits until the confirmation of the upgrade to supergroup through a message in the chat
    # and then it executes the addition of the description
    wait.until(ec.presence_of_element_located((By.XPATH, group_upgraded_message))).click()
    try:
        click(group_header_xpath)
    except ElementClickInterceptedException:
        wait.until(ec.invisibility_of_element((By.XPATH, popup_xpath)))
        click(group_header_xpath)


    click(modify_xpath)
    time.sleep(1)
    write(description_tab_xpath,f'Group of the course: {name}; Code: {code};')
    click(save_modification_xpath)

file.close()
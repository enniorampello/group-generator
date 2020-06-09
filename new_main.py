from constants import Constants
from time import sleep
import pyautogui as gui

TEXT_FILE_PATH = Constants.text_file_path

# open the file containing in each line the name of a group
file = open(TEXT_FILE_PATH, 'r')
lines = file.readlines()

# iterate through all the group names and create the corresponding Telegram groups
for line in lines:
    name = line.split(',')[0]
    code = line.split(',')[1].replace('\n','')
    sleep(1)
    gui.click(x=267, y=69) # Up left icon
    sleep(1)
    gui.click(x=203, y=121) # Crea gruppo
    sleep(1)
    gui.typewrite('g')
    gui.click(x=375, y=183) # Group Help bot
    sleep(1)
    gui.click(x=1399, y=68) # Avanti
    sleep(1)
    gui.typewrite(name)
    sleep(1)
    gui.click(x=1399, y=68) # Crea
    sleep(1)
    gui.click(x=386, y=59) # Group header
    sleep(1)
    gui.click(x=1399, y=68) # Modifica
    sleep(1)
    gui.click(x=779, y=312) # Descrizione
    sleep(1)
    gui.click(x=779, y=312)  # Descrizione
    sleep(1)
    gui.typewrite(f'Group of the course: {name}; Code: {code};')
    sleep(1)
    gui.click(x=1399, y=68)  # Fatto
    sleep(1)
    gui.click(x=1399, y=68)  # Modifica
    sleep(1)
    gui.click(x=654, y=552) # Amministratori
    sleep(1)
    gui.click(x=665, y=164) # Aggiungi amministratore
    sleep(1)
    gui.click(x=627, y=367) # group Help bot
    sleep(1)
    gui.click(x=720, y=756) # Fatto

    '''
    third course,157684
    fourth course,321321
    fifth course,789456
    sixth course,654963
    seventh course,357951
    '''
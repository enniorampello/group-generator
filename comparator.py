import csv
import pandas as pd

with open('group_names.txt', 'r') as gn, open('courses_triennale.csv', 'r') as ct, open('coursess.csv', 'w') as c:
    reader = csv.DictReader(ct)
    for new_course in reader:
        found = False
        for existing_course in gn.readlines():
            existing_course = existing_course.rstrip("\n")
            course = new_course['name']
            if course.lower() == existing_course.lower():
                found = True
                break
        gn.seek(0)
        if not found:
            print('writing...')
            if ',' in new_course['name']:
                c.write(new_course['id'] + ',"' + new_course['name'] + '"\n')
            else:
                c.write(new_course['id'] + ',' + new_course['name'] + '\n')
        
        



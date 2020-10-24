
# THIS IS THE SCRIPT THAT I USED TO CREATE A CSV FILE WITH THE INFO ABOUT
# THE EXISTING COURSES CONTAINED IN THE JSON FILE FROM GIORGIO PAIS

import json
import pandas as pd

with open(r'/Users/enniorampello/group-generator/database.json', 'r') as file:
    data = json.load(file)

courses = data.get('corsi')

courses_df = pd.DataFrame(courses)
courses_df = courses_df.transpose()
courses_df = courses_df[['code','name','link']]

courses_df.to_csv(r'/Users/enniorampello/group-generator/database.csv')
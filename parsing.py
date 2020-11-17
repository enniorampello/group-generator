import numpy as np

with open('scraped_courses_magistrale.txt', 'r') as f:
    lines = f.readlines()
    courses = []
    for line in lines:
        courses.append((line.split('/')[0], line.split('/')[1]))
array = np.array(courses)
unique = np.unique(array, axis=0)
with open('scraped_courses_magistrale_unique.txt', 'w') as o:
    for course in unique:
        if ',' in course[1]:
            o.write(str(course[0]) + ',"' + str(course[1]) + '"')
        else:
            o.write(str(course[0]) + ',' + str(course[1]))
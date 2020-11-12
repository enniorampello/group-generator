import csv

with open('group_names.txt', 'r') as names, open('database.csv', 'r') as db, open('missing_links.txt', 'w') as miss:
    reader = csv.DictReader(db)
    for name in names.readlines():
        name = name.rstrip("\n")
        found = False
        for row in reader:
            course = row['name']
            if course == name:
                found = True
                print(name + ' found!!!')
                break
        db.seek(0)
        if not found:
            miss.write(name + '\n')
        
        



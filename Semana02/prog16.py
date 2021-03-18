import csv

html_output = ''
names = []

with open('patrons.csv','r') as data_file:
    csv_data = csv.reader(data_file)

    #We dont' want headers or first line of band data
    next(csv_data)
    next(csv_data)

   
    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}" ) 




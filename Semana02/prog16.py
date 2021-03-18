import csv

html_output = ''
names = []

with open('patrons.csv','r') as data_file:
    csv_data = csv.reader(data_file)

    for line in csv_data:
        print(line)





# working with csv

import csv

# using reader and writer
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    #next(csv_reader) # nex is generator in python which throw away first line in csv

    #for line in csv_reader:
        #print(line[2])

    with open('new_names.csv', 'w', newline='') as new_csv_file:
        csv_writer = csv.writer(new_csv_file, delimiter='\t')
        
        for line in csv_reader:
            csv_writer.writerow(line)

# using DictReader and DictWriter
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    #for line in csv_reader:
        #print(line['email'])
    
    with open('new_names1.csv', 'w', newline='') as new_csv_file:
        field_names = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_csv_file, fieldnames=field_names, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)

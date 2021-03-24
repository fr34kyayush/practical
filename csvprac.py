import csv
f = open("LOCATION\\students.csv", 'r')
csv_reader = csv.reader(f)
for row in csv_reader:
    print(row)
f.close()

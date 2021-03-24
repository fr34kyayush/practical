import csv
f = open("C:\\Users\\Kanishka Juneja\\Documents\\students.csv", 'r')
csv_reader = csv.reader(f)
for row in csv_reader:
    print(row)
f.close()
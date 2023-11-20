import csv

f = open ('IS.csv')
csv_f = csv.reader(f)
data = []

for row in csv_f:
    data.append(row)
f.close()

print(data[1:])

def convert_row(row):

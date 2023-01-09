import csv
file= open("students.csv", "r")
reader= csv.reader(file)
fields = next(reader)
for row in reader:
    row.append(row)
print(row)
file.close()
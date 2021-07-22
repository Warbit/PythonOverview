import csv

with open("test.csv","w", newline="\n", ) as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "BOOK", "AUTHOR"])
    writer.writerow([1, "Beauty and the bestr","Mathira"])
    writer.writerow([2, "Ciderella", "John Alix"])
    writer.writerow([3, "Maat","Umera Ahmed"])

with open("test.csv","r") as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)
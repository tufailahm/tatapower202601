import csv
with open("h:\\helloproducts.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
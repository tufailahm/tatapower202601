import csv
total:int =0

with open("h:/meter.csv") as file:
    reader = csv.DictReader(file)

    for i in reader:
        total += int(i["unitsConsumed"])
        
print("Total units consumed:", total)
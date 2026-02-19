import csv

lowest_units = float('inf')
lowest_customer = None

with open("h:/meter.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        units = int(row["unitsConsumed"])
        if units < lowest_units:
            lowest_units = units
            lowest_customer = row["customerId"]

print("Customer with lowest consumption:", lowest_customer)
print("Units consumed:", lowest_units)
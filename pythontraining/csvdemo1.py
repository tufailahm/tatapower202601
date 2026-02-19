import csv
products = [
    {"productId": 1019, "productName": "Mouse","quantityOnHand":100, "price":99},
    {"productId": 1020, "productName": "Laptop","quantityOnHand":200, "price":88600},
    {"productId": 1021, "productName": "Mobile","quantityOnHand":300, "price":176000},
]
with open("h:\\helloproducts.csv","w",newline="") as file:
    fieldnames = ["productId" , "productName", "quantityOnHand" , "price"]
    writer = csv.DictWriter(file,fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(products)

print("Product details saved successfully")
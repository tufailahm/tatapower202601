#List is a collection which is ordered and changeable. 
# Allows duplicate members.
meter_details_neha = [19000, "Neha", "Bangalore", 5000, "Active"]
meter_details_neha[0] = 20000 # This will change the first element of the list to 20000
print("Neha Meter details")
for i in meter_details_neha:
    print(i)

#Tuple is a collection which is ordered and unchangeable.
# Allows duplicate members.

meter_details_ahmed = (19000, "Ahmed", "Bangalore", 5000, "Active")
print("Ahmed Meter details")
for i in meter_details_ahmed:
    print(i)
    
MAXIMUMLOAD = [10000, 20000, 30000] # This is a list which contains the maximum load values for different types of meters
MAXIMUMLOAD[0] = 15000 # This will change the first element of the list to 15000




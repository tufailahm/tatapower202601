total_consumption = int(input("Enter total consumption "))
gst = int(input("Enter gst rate"))

result = total_consumption + total_consumption/100*gst

print("Your net bill is ", result)
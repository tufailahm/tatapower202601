total_consumption = int(input("Enter total consumption"))
gst = int(input("Enter gst rate"))
result,surcharge =0,0

if total_consumption > 0 and total_consumption < 900 and gst < 100:
    result = total_consumption + total_consumption/100*gst
elif total_consumption>900:
    surcharge = 100
    result = total_consumption + total_consumption/100*gst +surcharge
else: 
    print("Please enter correct total consumption and gst")

print("Your net bill is ", result)
print(f"Your total consumption {total_consumption} and surcharge {surcharge} = Total Bill {result}")
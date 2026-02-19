total_consumption = int(input("Enter total consumption"))
gst = int(input("Enter gst rate"))
result =0

if total_consumption > 0 and gst < 100:
    result = total_consumption + total_consumption/100*gst
elif total_consumption>1000:
    surcharge = 1000
    result = total_consumption + total_consumption/100*gst + surcharge
else:
    print("Please enter correct total consumption(+0) and gst(>100)")

print("Your net bill is ", result)
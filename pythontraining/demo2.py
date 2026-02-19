cost,meter_reading,total_consumption=10000,760,890
customer_name,billAmount="Tarun",54000
print(type(billAmount))
billAmount = cost*meter_reading/total_consumption
gst = 18
billAmount += billAmount/100*gst
print(customer_name, " your total bill amount is ", billAmount)
print(type(billAmount))
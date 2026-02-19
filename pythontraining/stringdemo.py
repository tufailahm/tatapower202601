meter_readings= "MTRTATA918162"

print(meter_readings[0])
print(meter_readings[-4])

print(len(meter_readings))

text = "   hello python   "
print(text.strip())   # hello python
print(text.lstrip())  # hello python   
print(text.rstrip())  #    hello python

#Replace Text
print(text.replace("python", "Daysahead"))

langs = "Python,Java,SQL"
print(langs.split(","))

meter_details = "Tufail,12,8867205331,4"
meter_details_list = meter_details.split(",")


print(int(meter_details_list[1])+int(meter_details_list[3]))  # Tufail

#string is immutable
text.strip()   # hello python  
print(text)   #    hello python

OTP = "123456"
newOTP = OTP.replace("6","9") 

print(newOTP)  
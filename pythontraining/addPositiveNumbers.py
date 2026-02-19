i=1
result = 0
while(i<=5):
    num = int(input("Enter a positive number: "))
    i = i+1
    if num <0:
        continue
    result += num   
    
    
print("The sum of the positive numbers is: ", result)
load = int(input("Enter load value - "))

if load > 90:
    print("Critical!")
elif load > 75:
    print("Warning!")
elif load > 50:
    print("Caution!")
else:
    print("Normal")
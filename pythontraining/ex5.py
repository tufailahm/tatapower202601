grid_supply = (bool)(input("Is grid supply available? (True/False): "))
backup_supply = True

if (grid_supply == False):
    if (backup_supply == True):
        print("Backup supply is available")
    else:
        print("No power supply")
else:
    print("Grid supply is available")
meter_readings = [1000, 1520, 200, 250, 300]

meter_readings.append(350)  # Add a new reading to the list

meter_readings[2] = 220  # Update the reading at index 2

meter_readings.remove(250)  # Remove the reading with value 150

print("Meter Readings:", meter_readings)

meter_readings.sort()  # Sort the readings in ascending order
print("After sorting Meter Readings:", meter_readings)

# Calculate the total consumption
total_consumption = 0
for reading in meter_readings:
    total_consumption += reading
    
print("Total Consumption:", total_consumption)

#Print the maximum and minimum readings 
max_reading = max(meter_readings)
min_reading = min(meter_readings)
print("Maximum Reading:", max_reading)
print("Minimum Reading:", min_reading)
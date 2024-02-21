
# Task 1: Given the list of temparatures: Extract temperatures for the second week
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_temps = temperatures[7:14]
print("Second week temps:", second_week_temps)

# Task 2: Extracct all temps above 100
temps_above_100 = [temp for temp in temperatures if temp > 100]
print("Temps above 100:", temps_above_100)

# Task 3: Reverse temp list and extract temps from the 5th to the 10th day of reversed list
reversed_temp_list = list(reversed(temperatures))
temps_5th_to_10th = reversed_temp_list[4:10]
print("Temps from 5th to the 10th day reversed:", temps_5th_to_10th)
# Task 1: Sort the grades in descending order and display the sorted list

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)
print(grades)

# task 2: Calculate the average grade and display it
total_grades = sum(grades)
num_grades = len(grades)
average_grade = total_grades / num_grades
print("Average grade:", average_grade)

# Task 3: Replace any grade below 80 with the value 'Failed'
grades = ["Failed" if grade < 80 else grade for grade in grades]
print(grades)
         
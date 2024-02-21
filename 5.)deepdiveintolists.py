
# Task 1: Create a new list where each element is a dictionary with keys name, grade, and activity and the corresponding values from the provided lists.
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]


student_info_list = [{"name": name, "grade": grade, "activity": activity}for name, grade, activity in zip(students, grades, activities)]
print("New Dictionary list:", student_info_list)

# Task 2: Filter out students who have grades below 80
filtered_list = [student_info for student_info in student_info_list if student_info["grade"] >= 80]
print("Filtered student list:", filtered_list)

# Task 3:  For the remaining students, add a new key-value pair in their dictionary: "status": "Passed"
for student_info in filtered_list:
    student_info ["Status"] = "Passed"
print(filtered_list)
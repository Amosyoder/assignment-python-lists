
# Task 1: Determine which students both submitted their assignments and attended the class
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted_set = set(submitted)
attended_set = set(attended)
common_students = submitted_set.intersection(attended_set)
print(common_students)

# Task 2: Check if the two lists are identical in terms of their content
lists_identical = submitted == attended
if lists_identical:
    print("Lists are identical")
else:
    print("Lists are not identical")

# Task 3: using list method, remove any student from the attended list who did not submit their assignment
attended = [student for student in attended if student in submitted]
print("Updated attended list:", attended)

def calculate_average(students):
    """Calculates average marks for each student."""
    return {name: sum(marks) / len(marks) for name, marks in students.items()}

def find_top_performer(averages):
    """Finds the student with the highest average marks."""
    return max(averages, key=averages.get)

# Example Input
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
averages = calculate_average(students)
top_student = find_top_performer(averages)

print("Average Marks:", averages)
print("Top Performer:", top_student)

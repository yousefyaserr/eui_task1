def get_student_info():
 
  name = input("Enter student name: ")
  id = input("Enter student ID: ")
  return {"name": name, "id": id}

students = []  # List to store student information

while True:
  # Get student information
  student_info = get_student_info()

  # Add information to the list
  students.append(student_info)

  # Ask if user wants to add more students
  choice = input("Enter 'y' to add another student, or any other key to stop: ")
  if choice.lower() != 'y':
    break

# Print the collected information
print("\nStudent information:")
for student in students:
  print(f"Name: {student['name']}, ID: {student['id']}")

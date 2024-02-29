def get_student_info():
 
  name = input("Enter student name: ")
  id = input("Enter student ID: ")
  age=input("enter student age: ")
  return {"name": name, "id": id,"age": age}

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
  print(f"Name: {student['name']}\n ID: {student['id']}\n age:{student['age']}")

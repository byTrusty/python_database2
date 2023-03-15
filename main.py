# Define a list of dictionaries representing students
students = [
    { "name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow" },
    { "name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza" },
    { "name": "Julia", "hometown": "Houston", "favorite_food": "shrimp" }
]

# Define a function to list the names of all the students
def list_names(student_list):
    for i, student in enumerate(student_list):
        print(f"{i+1}. {student['name']}")

# Define a function to get a new student's information
def get_new_student():
    student = {}
    student["name"] = input("What is the student's name? ")
    student["hometown"] = input("Where is the student from? ")
    student["favorite_food"] = input("What is the student's favorite food? ")
    return student

# Start the main loop
while True:
    # Ask the user for their choice of action
    choice = input("What would you like to do? (add/view/quit) ")
    if choice == "quit":
        # Exit the loop and print a goodbye message
        print("Goodbye!")
        break
    elif choice == "view":
        # List the names of all the students and ask the user to select one
        list_names(students)
        selection = input("Enter the number of a student to view: ")
        try:
            selection_index = int(selection) - 1
            # Print the selected student's name and ask what information to display
            selected_student = students[selection_index]
            print(f"You selected {selected_student['name']}.")
            info_choice = input("Would you like to see their hometown or favorite food? ")
            if info_choice == "hometown":
                print(f"{selected_student['name']} is from {selected_student['hometown']}.")
            elif info_choice == "favorite food":
                print(f"{selected_student['name']}'s favorite food is {selected_student['favorite_food']}.")
            else:
                print("Invalid choice. Please try again.")
        except (ValueError, IndexError):
            # Handle errors if the user enters an invalid selection
            print("Invalid selection. Please try again.")
    elif choice == "add":
        # Get information for a new student and add them to the list
        new_student = get_new_student()
        students.append(new_student)
    else:
        # Handle errors if the user enters an invalid choice
        print("Invalid choice. Please try again.")

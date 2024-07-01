# Student Grade Tracker

# Initialize an empty dictionary to store student grades
student_grades = {}

def add_subject():
    # Ask user to input subject name
    subject = input("Enter subject name: ")
    # Ask user to input grade for the subject
    grade = float(input("Enter grade for {}: ".format(subject)))
    # Add subject and grade to the dictionary
    student_grades[subject] = grade
    print("Grade added for {}".format(subject))

def calculate_average():
    # Calculate the average grade
    total = sum(student_grades.values())
    average = total / len(student_grades)
    print("Average grade: {:.2f}".format(average))

def display_grades():
    # Display all grades
    print("Grades:")
    for subject, grade in student_grades.items():
        print("{}: {:.2f}".format(subject, grade))

def main():
    while True:
        print("Student Grade Tracker")
        print("1. Add subject and grade")
        print("2. Calculate average grade")
        print("3. Display all grades")
        print("4. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_subject()
        elif choice == "2":
            calculate_average()
        elif choice == "3":
            display_grades()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
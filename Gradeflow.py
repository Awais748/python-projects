
students=[]


def get_grade(marks):
    if marks >=90:
        return "A"
    elif marks >=80:
        return "B"
    elif marks >=70:
        return "C"
    elif marks >=60:
        return "D"
    else:
        return "F"
    
def add_student():
    student_name = input("Enter student name:")
    student_marks = int(input(f"Enter {student_name}'s marks (0-100):"))
    students.append((student_name, student_marks))
    print(f"{student_name} added successfully")


def print_report():
    if not students:
        print(" No students added yet")
        return 
    
    print(f"\n{"Name":<12} {"Marks":<8} {"Grade":<8} {"Status"}")
    print("-" * 38)


    for student_name, student_marks in students:
        grade = get_grade(student_marks)
        status = "Pass" if grade != "F" else "Fail"
        print(f"{student_name:<12} {student_marks:<8} {grade:<8} {status}")


def show_summary():
    if not students:
        print(" No students added yet!")
        return
    passed = [name for name , marks in students if get_grade(marks) != "F" ]    
    failed = [name for name , marks in students if get_grade(marks) == "F"]
    top    = [name for name, marks in students if get_grade(marks) == "A"]

    print(f"\n  Total Students : {len(students)}")
    print(f"  Passed         : {passed}")
    print(f"  Failed         : {failed}")
    print(f"  Top Students   : {top if top else 'None'}")
    

def search_student():
    query = input("Enter student name to search: ").strip()
    names = [name for name, _ in students]

    if query in names:
        marks  = [m for n, m in students if n == query][0]
        grade  = get_grade(marks)
        status = "Pass" if grade != "F" else "Fail"
        print(f"\n  Name   : {query}")
        print(f"  Marks  : {marks}")
        print(f"  Grade  : {grade}")
        print(f"  Status : {status}")
    else:
        print(f"  '{query}' not found in system!")

def main():
    print("=" * 38)
    print("   GradeFlow — Student Result Manager")
    print("=" * 38)

    while True:
        print("\n  1. Add Student")
        print("  2. View Report")
        print("  3. Show Summary")
        print("  4. Search Student")
        print("  5. Exit")

        choice = input("\n  Choose option (1-5): ").strip()

        match choice:
            case "1": add_student()
            case "2": print_report()
            case "3": show_summary()
            case "4": search_student()
            case "5":
                print("\n  GradeFlow closed. Good luck!")
                break
            case _:
                print("  Invalid option! Choose 1-5")        

if __name__ == "__main__":
    main()                
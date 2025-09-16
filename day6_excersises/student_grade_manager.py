def add_student(students,name,grade):
    students.append((name,grade))
    print(f"{name} added with {grade}")

def display_student(students):
    if not students:
        print("no students available")
    else:
        print("\n---students list")
        #enumerate student gives each student a number(1,2,3,4...)
        for i, (name,grade) in enumerate (students, start=1):
            print(f"{i}.{name}-{grade}")
        print("-------------------\n")

def top_student(students):
    if not students:
        print("no students available")
        return
    best=max(students,key=lambda s: s[1])
    print(f"🏆 Top student is {best[0]} with grade {best[1]}")

students=[]
while True:
    print("\n--- Student Grade Manager ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Show Top Student")
    print("4. Exit")
    choice = input("enter your choice:1-4): ")

    if choice == "1":
        name = input("enter student name: ")
        grade = float(input("enter student grade: "))
        add_student(students, name, grade)
    elif choice == "2":
        display_student(students)
    elif choice == "3":
        top_student(students)
    elif choice == "4":
        print("exiting program")
    else:
        print("invalid choice")


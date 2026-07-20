import json

FILENAME = "Students/students_db.json"

class Student:
    def __init__(self, name: str, roll_num: int, grade: str):
        self.name = name
        self.roll_num = roll_num
        self.grade = grade


    def to_dict(self):
        return {
            "name": self.name,
            "roll_number":  self.roll_num,
            "grade": self.grade
        }
    
    def __str__(self):
        return f"Name: {self.name} | Roll_Number: {self.roll_num} | Grade: {self.grade}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if all(char.isalpha() or char == " " for char in new_name):
            self.__name = new_name
        else:
            raise ValueError("Name Must Not Contain Numbers")


    @property        
    def roll_num(self):
        return self.__roll_num

    @roll_num.setter
    def roll_num(self, new_roll_num):
        if isinstance(new_roll_num, int):
            self.__roll_num = new_roll_num
        else:
            raise ValueError("Roll Number Must Be an Integer Only")


    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, new_grade):
        if new_grade.upper() in ["A","B","C","D","E","F"]:
            self.__grade = new_grade.upper()
        else:
            raise ValueError("Grade Must Be only (A, B, C, D, E or F)")
            



class StudentManager:
    def __init__(self, filename = FILENAME):
        self.filename = filename
        self.students = []
        self.load_db()

    def load_db(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            for item in data:
                student_obj = Student(item["name"], item["roll_number"], item["grade"])
                self.students.append(student_obj)
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []
                    
        
    
    def save_data(self):
        json_data = [item.to_dict() for item in self.students]

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2, ensure_ascii=False)




    def add_student(self, student_obj: Student):
        self.students.append(student_obj)
        self.save_data()        
        print(f"\nStudent {student_obj.name} Was Successfully Added!") 


    def show_all_students(self):
        if not self.students:
            print("\nNo students found in the database.")
            return

        print("\n====== Student's List =====")
        for item in self.students:
            print(item) 
        print("===========================\n")


    def search_student(self, roll_number):
        for item in self.students:
            if item.roll_num == roll_number:
                print(f"\nStudent Found:")
                print(item) 
                return 
        print(f"\nStudent With Roll Number ({roll_number}) Does Not Exist.")


    def update_grade(self, roll_number: int, new_grade: str):
        for item in self.students:
            if item.roll_num == roll_number:
                try:
                    item.grade = new_grade
                    self.save_data()
                    print(f"\nGrade successfully updated for {item.name}!")
                    return 
                except ValueError as e:
                    print(f"\nUpdate Failed: {e}")
                    return

        print(f"\nStudent with Roll Number {roll_number} not found.")


#  ვალიდაციის ფუნქციები
def get_choice(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if choice in [1, 2, 3, 4, 5]:
                return choice
            print("Error: Choose between 1 and 5 only!\n")
        except ValueError:
            print("Error: Enter Numbers Only!\n")

def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()

        if not name:
            print("Error, Name Can Not Be Empty!")
            continue
        if all(char.isalpha() or char == " " for char in name):
            return name.title()
        print("Error: Name Must Contain Letter And Spaces Only!")

def get_valid_roll(prompt, manager_obj: StudentManager):
    while True:
        try:
            roll = int(input(prompt))
            if any(item.roll_num == roll for item in manager_obj.students):
                print(f"Error: Roll Number {roll} Is Already Taken!\n")
                continue
            return roll
        except ValueError:
            print("Error: Roll Must Be An Integer")

def get_valid_grade(prompt):
    while True:
        grade = input(prompt).strip().upper()
        if grade in ["A", "B", "C", "D", "E", "F"]:
            return grade
        print("Error: Grade must be A, B, C, D, E, or F!")



# ===== მთავარი პროგრამა =====
print("=" * 10, "Student Manager", "=" * 10, "\n")

manager = StudentManager()

while True:

    print("1. Add New Student")
    print("2. Show All Students")
    print("3. Search For a Student")
    print("4. Update Grade")
    print("5. Exit program\n")

    user_choice = get_choice("Choose Between (1-5): ")

    if user_choice == 1:
        print("\n--- Add New Student ---")

        name = get_valid_name("Enter Name: ")
        roll_num = get_valid_roll("Enter Roll NUmber: ", manager)
        grade = get_valid_grade("Enter Grade (A-F): ")

        new_student = Student(name, roll_num, grade)
        manager.add_student(new_student)

    elif user_choice == 2:
        manager.show_all_students()
    
    elif user_choice == 3:
        print("\n--- Search Student ---\n")

        try:
            roll_search = int(input("Enter Roll Number To Search: "))
            manager.search_student(roll_search)
        except ValueError:
            print("Error: Roll Number Must Be An Integer")
    
    elif user_choice == 4:
        print("\n--- Update Student Grade ---\n")
        try:
            roll_to_find = int(input("Enter Student's Roll Number: "))

            new_grade = get_valid_grade("Enter New Grade (A-F): ")

            manager.update_grade(roll_to_find, new_grade)
        except ValueError:
            print("Error: Roll Number Must Be a Number")

    elif user_choice == 5:
        print("\n Goodbye! Student Manager Closed")
        break
    
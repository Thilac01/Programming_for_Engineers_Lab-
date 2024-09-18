class EngStudent:
   
    def __init__(self, stu_name, e_no):
        self.name = stu_name
        self.e_num = e_no

  
    def print_student_info(self):
        print("Name:", self.name, ", E-No:", self.e_num)

   
    def change_name(self, new_name):
        self.name = new_name


    def change_enum(self, new_enum):
        self.e_num = new_enum


student_1 = EngStudent("Chathura Gamage", "E/22/107")
student_2 = EngStudent("Yasitha Rajapaksha", "E/22/274")

student_1.print_student_info()
student_2.print_student_info()


student_1.change_enum("E/22/206")

student_1.print_student_info()


students = {
    "Isuru Pamuditha": "E/22/206",
    "Thilina Dissanayake": "E/22/001",
    "Shakthi Perera": "E/22/181"
}


eng_stu_list = []


for name, enum in students.items():
    eng_stu_list.append(EngStudent(name, enum))


print("Type of elements in list:", type(eng_stu_list[0]))

for student in eng_stu_list:
    student.print_student_info()

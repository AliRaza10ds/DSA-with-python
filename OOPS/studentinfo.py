class student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
    
    def name(self):
        return (f"Name :{self.name} ")
    
    def roll(number):
        return (f"ROll No : {self.roll_number}")
    
student_roll_input=int(input("Enter the roll number"))
student_name=input("Enter your name")
    
student_name_info=student.name(student_name)
print(student_name_info)
student_roll_info=student.roll(student_roll_input)
print(student_name_info)
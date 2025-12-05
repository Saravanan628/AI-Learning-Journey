from functools import reduce

class Student:
    def __init__(self,num_of_sub):
        self.num_of_sub=num_of_sub

    def get_input_marks_Percent(self):
        marks=[]
        for i in range(self.num_of_sub):
            marks.append(int(input("Enter marks: ")))
        total=reduce(lambda a,b:a+b,marks)
        percent=total/len(marks)
        return percent

s1=Student(5)
print(s1.get_input_marks_Percent())




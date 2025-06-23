#This is the code to test each of your classes
#You can cut out any sections you don't want to test (eg if you know it will crash)

#Import classes from external files - the first one is done - you add the rest
from headTeacher import *
from primaryStudent import *
from highSchoolStudent import *
from subject import *
from task import *

#Define any subprograms you might need here


#The mainline program code 
#Test the classes by adding one object of each and interacting with their methods to ensure they behave correctly

#Code to test the Subject class
print('-'*10+"Testing Subject class"+"-"*10)
subject=Subject("Software Engineering", "TAS")
print(f"{subject.info()}")
subject2=Subject("Textiles & Design", "TAS")
print(f"{subject2.info()}\n")

#Code to test the Person class
print('-'*10+"Testing Person class"+"-"*10)
p=Person("Polly")
print(p.info())
print(p.getName())
p.setName("Penny")
print(f"Name after change={p.getName()}\n")

#Code to test the Staff class
print('-'*10+"Testing Staff class"+"-"*10)
staff=Staff("Ms Phair",200000)
print(staff.info())
staff.giveRaise(1000)
print(f"Salary after $1000 raise=${staff.getSalary()}\n")

#Code to test Teacher class
print('-'*10+"Testing Teacher class"+"-"*10)
teacher=Teacher("Mr Lemmon",100000)
print(teacher.info())
teacher.giveRaise(1000)
print(f"Salary after $1000 raise=${teacher.getSalary()}")
teacher.enrol(subject)
print(f"After enrolling in a subject, {teacher.getName()} is enrolled in {teacher.getSubjects()[0].getName()}\n")

#Code to test the HeadTeacher class
print('-'*10+"Testing HeadTeacher class"+"-"*10)
headTeacher=HeadTeacher("Ms Turner",150000, [], "TAS")
print(headTeacher.info())
headTeacher.giveRaise(1000)
print(f"Salary after $1000 raise=${headTeacher.getSalary()}")
headTeacher.enrol(subject2)
print(f"After enrolling in a subject, {headTeacher.getName()} is enrolled in {headTeacher.getSubjects()[0].info()}\n")

#Code to test the Student class
print('-'*10+"Testing Student class"+"-"*10)
student=Student("Stewart", 8)
print(student.info())
student.nextSchoolYear()
print(f"After going up a year, {student.getName()} is in year {student.getSchoolYear()}\n")

#Code to test the PrimaryStudent class
print('-'*10+"Testing PrimaryStudent class"+"-"*10)
primaryStudent=PrimaryStudent("Priya", 5, teacher)
print(primaryStudent.info())
primaryStudent.nextSchoolYear()
print(f"After going up a year, {primaryStudent.getName()} is in year {primaryStudent.getSchoolYear()}")
print(f"{primaryStudent.getName()}'s teacher is {primaryStudent.getTeacher().getName()}\n")

#Code to test the HighSchoolStudent class
print('-'*10+"Testing HighSchoolStudent class"+"-"*10)
highSchoolStudent=HighSchoolStudent("Harry", 11, [])
print(highSchoolStudent.info())
highSchoolStudent.nextSchoolYear()
highSchoolStudent.enrol(subject)
highSchoolStudent.enrol(subject2)
print(f"After going up a year and enrolling in 2 subjects {highSchoolStudent.info()}")
highSchoolStudent.remove(subject2)
print(f"After removing 1 subject, {highSchoolStudent.getName()} is enrolled in {highSchoolStudent.subjects[0].getName()}\n")


#Code to test the Task class
print('-'*10+"Testing Task class"+"-"*10)
task=Task("OOP validation task", 45)
subject.addTask(task)
print(f"{subject.getName()} now has task {subject.getTasks()[0].getName()}")
task.setMark(student,32)
task.setMark(highSchoolStudent, 41)
task.setMark(primaryStudent,18)
print(f"Marks entered for {task.getName()} (out of {task.maxMark}):")
for student in task.getMarks():
    print(f"\t{student.getName()} (Yr {student.getSchoolYear()}) {task.getMark(student)}")
print(task.info())

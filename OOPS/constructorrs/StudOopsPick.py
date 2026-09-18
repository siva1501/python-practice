import sys, pickle
from Student import Student


class StudPick:
    def savestudentdata(self):
        with open("oopsstu.data", "ab") as fp:
            while True:
                print("*" * 50)
                sno = int(input("Enter the student number:"))
                sname = input("Enter the Stdent Name:")
                marks = float(input("Enter the Student Marks:"))
                s = Student(sno, sname, marks)  # calling pc of student calss
                pickle.dump(s, fp)
                print("Student data save in the file.")
                print("*" * 50)
                ch = input("Do u wnat to insert another record (yes/no):")
                if ch.lower() == "no":
                    print("thanks for using this program")
                    print("*" * 50)
                    sys.exit()


# main program
sp = StudPick()
sp.savestudentdata()

Python Constructors

A constructor is a special method in a class that is automatically called when an object is created.

1. Constructor name

In Python, the constructor is:

__init__()

Example:

class Student:

    def __init__(self):
        print("Constructor called")

s1 = Student()

Output:

Constructor called

When we write:

s1 = Student()

Python automatically calls:

__init__()
2. Constructor with data

We can use a constructor to initialize object data.

class Student:

    def __init__(self, sno, sname):
        self.sno = sno
        self.sname = sname

    def display(self):
        print("Student Number:", self.sno)
        print("Student Name:", self.sname)


s1 = Student(101, "Siva")
s1.display()

Output:

Student Number: 101
Student Name: Siva

Here:

__init__() → constructor
self → current object
sno → student number
sname → student name
self.sno and self.sname → object-level data members
3. Constructor is called automatically

You do not normally call the constructor separately.

❌ Not needed:

s1.__init__(101, "Siva")

✅ Normally:

s1 = Student(101, "Siva")
4. Types of constructors

In beginner-level Python, constructors are commonly discussed as:

Default constructor
Parameterized constructor
Default constructor

Takes only self.

class Student:

    def __init__(self):
        self.sno = 101
        self.sname = "Siva"

s1 = Student()

print(s1.sno)
print(s1.sname)
Parameterized constructor

Takes additional parameters.

class Student:

    def __init__(self, sno, sname):
        self.sno = sno
        self.sname = sname

s1 = Student(101, "Siva")
Easy definition to remember

A constructor is a special __init__() method that is automatically executed when an object is created and is mainly used to initialize object data.
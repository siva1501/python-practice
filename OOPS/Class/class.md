1. What is a Class?

A class is a blueprint/template for creating objects.

Think about a house blueprint 🏠:

Blueprint → Class
Actual houses built from it → Objects

For example, if we want to represent a student:

class Student:
    pass

Here, Student is a class.

2. What is an Object?

An object is an instance of a class.

class Student:
    pass


student1 = Student()
student2 = Student()

Here:

Student → class
student1 → object
student2 → object

We can create many objects from one class.

             Student (Class)
                  |
          -------------------
          |                 |
      student1           student2
       (Object)           (Object)
3. Class with Data Members

A class can contain data.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

Create an object:

student1 = Student("Siva", 22)

print(student1.name)
print(student1.age)

Output:

Siva
22
What happened?

When we write:

student1 = Student("Siva", 22)

Python creates an object and calls:

__init__()

Then:

self.name = name
self.age = age

stores data inside that particular object.

4. What is self?

This is very important in Python OOP.

self refers to the current object.

Example:

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

When we do:

student1 = Student("Siva", 22)

Conceptually:

student1
   |
   |---- name = "Siva"
   |
   |---- age = 22

And:

student2 = Student("Ravi", 20)

creates another object:

student2
   |
   |---- name = "Ravi"
   |
   |---- age = 20

So self allows each object to have its own data.

5. Methods

A method is a function inside a class.

Example:

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

Now:

student1 = Student("Siva", 22)

student1.display()

Output:

Siva
22

Here:

def display(self):

is a method.

6. Class = Data + Methods

This is one of the most important ideas.

class Student:

    # Data
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Behavior
    def display(self):
        print(self.name)
        print(self.age)

So:

Class
 |
 ├── Data Members
 │      ├── name
 │      └── age
 │
 └── Methods
        └── display()
Simple definition

Class is a blueprint that contains data members and methods used to create objects.

7. Class vs Object
Class	                                 Object
Blueprint	                       Actual instance
Logical                            concept Real instance created in memory
Student	                           student1
Used to create objects	           Created from a class

Example:

class Car:
    pass

Car → Class

car1 = Car()
car2 = Car()

car1 and car2 → Objects.

8. One Simple Real-Life Example

Imagine a Bank Account.

The class defines what every account should have:

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        print(self.name)
        print(self.balance)

Create objects:

account1 = BankAccount("Siva", 10000)
account2 = BankAccount("Ravi", 5000)

Now:

account1.display()

Output:

Siva
10000

And:

account2.display()

Output:

Ravi
5000

The same class is used to create different objects with different data.

⭐ Remember this structure
                 CLASS
                   |
        -----------------------
        |                     |
   Data Members            Methods
        |                     |
   name, age             display()
        |
        ↓
      OBJECT
        |
   student1

And the basic Python syntax is:

class ClassName:

    def __init__(self, data):
        self.data = data

    def method(self):
        # code


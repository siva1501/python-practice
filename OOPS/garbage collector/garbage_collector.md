		======================================
				Destructors in Python
				    and 
				Garbage Collector
		======================================
=>We know that Garbage Collector is one of the in-built program in python, which is running behind of every python program and whose role is to collect un-used memory space and it improves the performance of python based applications.
=>Every Garbage Collector Program is internally   calling its Own Destructor Function.
=>The destructor function  name in python is   def  __del__(self).
=>By default ,The destructor always called by Garbage Collector  when the program execution completed  for de-allocating the memory space of objects which are used in that program. Where as constructor called By PVM implicitly during object  creation for initlizing the object.

=>When the program execution is completed, GC calls its own destructor to de-allocate the memory space of objects present in program and it is called automatic Garbage Collection.
=>Hence , We have THREE programming  conditions for calling GC  and  to make the garbage collector to call destructor Function.

a) By default (or) automatically  GC calls destructor, when the program execution completed(called automatic Garbage Collection).
b) Make the object reference as None  for calling Forcefull Garbage Collection( called Forcefull Garbage Collection)
				Syntax :   objname=None
c) delete the object by using del operator  for calling Forcefull Garbage Collection(Called Forcefull Garbage Collection)
					Syntax:-   del  objname

-----------------
=>Syntax:
-----------------
		def       __del__(self):
		           -----------------------
			   -----------------------
=>No Need to write destructor in class of Python bcoz GC contains its own Destructor 
=================================================================================================
				Garbage Collector
----------------------------------------------------------------------------------------------------------------------------------------------------------------
=>Garbage Collector contains a pre-defined module called "gc"
=>Here gc contains the following  Functions.
			
			1) isenabled()
			2) enable()
			3) disable()
=>GC is not under the control of Programmer but it always maintained and mangaged by OS and PVM.
NOTE: Python Programmers need not to write destructor method / function and need not 
            to deal with Garbage Collection Process by using gc module bcoz PVM and OS takes care about Automatic Garbage Collection Process by automatic enabling of GC .
==============================================x===================================================



Garbage Collector in Python

A Garbage Collector (GC) is a part of Python that automatically removes objects that are no longer needed.

1. Why do we need a Garbage Collector?

When we create an object:

s = Student()

Python allocates memory for the Student object.

If the object is no longer used:

s = None

the object may become unreachable.

Python's Garbage Collector identifies such unused objects and releases their memory.

2. Simple example
class Student:
    pass

s1 = Student()
s2 = Student()

s1 = None
s2 = None

After s1 = None and s2 = None, the Student objects are no longer referenced.

The Garbage Collector can clean them up.

3. __del__() method

Python provides a special method called __del__().

It can be called when an object is being destroyed:

class Student:

    def __del__(self):
        print("Object destroyed")

s = Student()

s = None

Possible output:

Object destroyed

⚠️ __del__() should not be relied on for important resource cleanup because the exact timing of its execution is not guaranteed.

4. Reference counting

Python primarily keeps track of how many references point to an object.

s1 = Student()
s2 = s1

Now both s1 and s2 refer to the same object.

s1 ──┐
     ├──> Student object
s2 ──┘

If:

s1 = None

there is still one reference (s2).

If:

s2 = None

there are no references left, so the object becomes eligible for cleanup.

5. Circular references

Sometimes objects refer to each other:

Object A → Object B
   ↑         ↓
   └─────────┘

Even when the program can no longer reach these objects, their reference counts may not become zero.

Python's cyclic garbage collector can detect and clean up these cycles.

6. gc module

Python provides the gc module to work with garbage collection.

import gc

print(gc.isenabled())

To manually request a garbage-collection cycle:

gc.collect()
Remember for interviews ⭐

Garbage Collector:

A Python mechanism that automatically identifies and frees memory occupied by objects that are no longer reachable or needed.

Main points:

Automatic memory management
Uses reference counting
Handles cyclic references
gc module provides control over cyclic GC
__del__() is related to object finalization, but shouldn't be treated as a guaranteed cleanup mechanism


		=================================================
						Introduction to Inheritance 
		=================================================
=>Inhenritance is one of distinct features of OOPs
=>The purpose of Inheritance is that " To build Re-usable Applications with Effective Memmory Management in Python Object Oriented  Programming".
-----------------------------------------
=>Definition of Inheritance:
------------------------------------------
=>The Process obtaining Data members , Methods and Constructors (Features ) of one class   into  another class is called Inheritance.
=>The class which is giving Data members , Methods and Constructors (Features ) is called  Super or  Base or Parent Class.
=>The Class which is taking Data members , Methods and Constructors (Features ) is called  Sub or  Derived or Child Class.
=>The Inheritance concept always follows Logical OR Virtual  Memory Management. This Memory Management says that " Neither we write Source Code nor Takes Physical Memory Space ".
-------------------------------------------------------------------------------------------------------------------------------------
Advatnages of Inheritance:
----------------------------------------------------------------------------------
=>When we develop any inheritance based application, we get the following advantages.
		1. Application Development Time is Less
		2. Application Memory Space is Less
		3. Application Execution time is Fast / Less 
		4. Application Performance is enhanced (Improved )
		5. Redundency (Duplication ) of the code is minimized.
---------------------------------------------------------------------------------------------------------------------------------------------------------

			==========================================================
					Inheriting the Features of Base Class into Derived Class
			==========================================================
To Inherit the Features of Base Class into Derived Class, we use the following Syntax:

		class <clsname-1>:
			-----------------
			-----------------
		class <clsname-2>:
			-----------------
			-----------------
		class <clsname-n>:
			-------------------
			-------------------
		class <clsname-n+1>(clsname-1,clsname-2,.....,clsname-n):
			------------------------
			------------------------
--------------------------------------
Explanation
--------------------------------------
=>Here <clsname-1>,<clsname-2>,....<clsname-n> are called Base / Super Classes
=>Here <clsname-n> Represents Name of Derived Class.
=>This Syntax Makes us to Understand, All the Features of Base Class(es) are Virtually Inherited into Derived Class and we 
    can access them w.r.t to an object of Derived Class .
=>When we develop any Inheritance Based Application, It is always recommended to create an object of Bottom Most 
     Derived Class bcoz It Inherits the Features of Base Class and intermediate Base Class(es).
=>For Every Class, There exist an Implicit Pre-Defined Super Class Called 'object' bcoz It provides Garbage Collection Facility to Collect Un-used Memory space and improves the Performnace of Python Based Applications.
=>Hence For all the Data types (Classes), there is super type called 'object'.
---------------------------------------------------------------------------------------------------------------------------------------------------------

					===================================================
							 Types of Inheritances 
					===================================================
=>The Types of Inheritance is a Model / Pattern / Diagram, which Makes us to understand, How the Features are inherting from Base Class into Derived Class.
=>In Python Programming, we have 5 Types of Inheritances
				1. Single Inheritance
				2. Multi Level Inheritance
				3. Hierarchical Inheritance
				4. Multiple Inheritance
				5. Hybrid Inheritance


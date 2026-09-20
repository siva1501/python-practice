			==================================================
					Polymorphism in Python
			==================================================
=>The Polymorphism is one of the Best Principle in OOP Lang
=>The Advantage of Polymorphism is that "To Take Less Memory Space"
=>The Process of Representing "One Form in Multiple Forms" is called Polymorphism
=>One Form Represents Original Method
=>Multiple Forms Represents Overridden Methods
=>A Form is Nothing But State of Existence of Method. If the Method Exist in Base Class then It is called Original Method and If the method exist in Derived Class then It is called Overridden Methods.
=>To Implement Polymorphism in Python Lang, we Have Two Programming Concepts. They are
					1. Method Overriding
					2. Constructor Overriding
------------------------------------------------------------------------------------------------------------------------------------------------

		===========================================
			Method Overriding in Python
		===========================================
=>Method Overriding=Method Heading is same + Method Body is Different
			(OR)
=>The process of re-defining the original method of base class into various derived classes for performing different operations is called Method Overriding.
=>To use Method Overriding in python program we must apply Inheritance Principle.
=>Method Overriding used for implementing Polymorphism Principle.
    ( PLOYMORPHISM<----METHOD OVERRIDING<-----INHERITANCE<----CLASS AND OBJECTS )
-------------------------------------------------------------------------------------------------------------------------------------------------------



		===========================================
			Constructor Overriding in Python
		===========================================
=>Constructor Overriding=Constructor Heading is same + Constructor Body is Different
			(OR)
=>The process of re-defining the original Constructor of base class into various derived classes for Initlizing  different Obejcts with Different values  is called Constructor Overriding.
=>To use Constructor Overriding in python program we must apply Inheritance Principle.
=>Constructor Overriding used for implementing Polymorphism Principle in Python
    ( POLYMORPHISM<----Constructor OVERRIDING<-----INHERITANCE<----CLASS AND OBJECTS )
-------------------------------------------------------------------------------------------------------------------------------------------------------

	=====================================================================================
	Number of approaches to call original methods / constructors  from Overridden methods / Constructors
	=====================================================================================
=>We have two approches to call original method / constructors of base class from overridden method / constructors of derived class. They are

	1) By using   super()
	2) By using Class Name
------------------------------------------------------------------------
1) By using   super():
------------------------------------
=>super() is one of the pre-defined function, which is used for calling super class  original method / constructor from overridden method / constructors of derived class.

Syntax1:-       super().methodname()
		         super().__init__()

=>with super() we are able to call only immediate base class method / Constructor but unable to call Specified method / Constructor  of base Class . To do this we must use class name approach.
----------------------------------------------------------------
2) By using Class Name:
----------------------------------------------------------------
=>By using ClassName approach, we can call any base class method / constructor name from the context of derived class method / constructor names.

Syntax1:-      	ClassName.methodname(self)
			ClassName.__init__(self)
------------------------------------------------------------------------------X--------------------------------------------------------------------------
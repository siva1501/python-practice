while(True):
    try:
        print("program Start")
        s1=int(input("enter tha value of s1:"))
        s2=int(input("enter tha value of s2:"))
        a=s1
        b=s2
        c=a/b
        print(c)
    except ZeroDivisionError:
        print("PLEAS DO NOT ENTER THE ZERO")
    except ValueError:
        print("PLEAS DO NOT ENTER STRING AND SYMBOLES ETC... ONLY INTER THE NUMBERS")
    else:
        print("s1 is {}".format(a))
        print("s2 is {}".format(b))
        print("div is {}".format(c))
        print("program is completed")
    finally:
        print("im funal block")




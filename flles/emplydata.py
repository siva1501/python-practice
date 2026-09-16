import pickle,sys
with open("emp.data","ab") as fp:
    # print("//"*50)
    # print("\tEmpno\t name/tsal")
    # print("//"*50)
    while(True):
        eno=input("Enter the Employee Number:")
        ename=input("enter the name of the Employee:")
        sal=float(input("Enetr sal:"))
        l=[eno,ename,sal]
        pickle.dump(l,fp)
        ch=input("Do youn want entyer anthe emp data(yes/no)")
        if(ch.lower()=="no"):
            print("tnx")
            sys.exit()


        # try:
        #     obj=pickle.load(fp)
        #     for val in obj:
        #         print("\t{}".format(val),end="")
        #     print()
        # except EOFError:
        #     print("//"*50)
        #     break
        # except FileExistsError:
        #     print("file not found")
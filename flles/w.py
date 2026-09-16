obj={10,20,10,3,40,50,"siva"}
k={"name":"siva","age":22,"marks":100}
with open("stud5.data","w") as fp:
    print("/"*100)
    print("File opne in write mode")
    print("Name of yhe file:",fp.name)
    print("mode of the file:",fp.mode)
    print("type() fp",type(fp))
    print("is the file writeable:",fp.writable())
    print("is the file readable:",fp.readable())
    print("/"*100)
    fp.write("Siva shankara reddy\n")
    fp.write("Address:ramachandrapuram,house no:3-4,main road\n")
    fp.write("He id b,tech compled\n")
    fp.write("search for job\n")
    fp.writelines(str(obj)+"\n")
    fp.writelines(str(k))


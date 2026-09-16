try:
    fp = open("siva1.data", "r")

except FileNotFoundError:
    print("File does not exist")

else:
    print("File opened successfully in read mode")
    print("Type:", type(fp))
    print("File name:", fp.name)
    print("File mode:", fp.mode)

finally:
    print("\nI am from the finally block")
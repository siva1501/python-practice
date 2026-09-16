#Tuple
# 1.list to tuple
l1=[1,2,3,4,5,6,"siva"]
print(l1,type(l1))
t1=tuple(l1)
print(t1,type(t1))
print("/"*100)

# 2.set to tuple
s1={1,2,3,4,5,6,"siva"}
print(s1,type(s1))
t1=tuple(s1)
print(t1,type(t1))
print("/"*100)

# 3.forzenset to tuple
s1={1,2,3,4,5,6,"siva"}
s11=frozenset(s1)
print(s11,type(s11))
t1=tuple(s11)
print(t1,type(t1))
print("/"*100)

# dict to tuple
d1={1:10,2:20,3:30}
print(d1,type(d1))
t1=tuple(d1.items())
print(t1,type(t1))
print("/"*100)




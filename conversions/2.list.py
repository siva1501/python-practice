#LIST
# 1.tuple to list
t1=(1,2,3,4,5,6,"siva")
print(t1,type(t1))
l1=list(t1)
print(l1,type(l1))
print("/"*100)

# 2.set to list
s1={1,2,3,4,5,6}
print(s1,type(s1))
l1=list(s1)
print(l1,type(l1))
print("/"*100)

# 3.forzenset to list
s1={1,2,3,4,5,6}
s11=frozenset(s1)
print(s11,type(s11))
l1=list(t1)
print(l1,type(l1))
print("/"*100)

# 4.dict to list
d1={1:10,2:20,3:30}
print(d1,type(d1))
l1=list(d1.items())
print(l1,type(l1))
print("/"*100)

# 5.str to list
s="siba"
print(s,type(s))
l=list(s)
print(l,type(l))
print("/"*100)


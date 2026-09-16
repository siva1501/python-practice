#set
# 1.list to set
l=[1,2,3,4,5,6,"siva"]
print(l,type(l))
s1=set(l)
print(s1,type(s1))
print("/"*100)

# 2.tuple to set
t=(1,2,3,4,5,6,"siva")
print(t,type(t))
s1=set(t)
print(s1,type(s1))
print("/"*100)

# 3.forzenset to set
t=(1,2,3,4,5,6,"siva")
f1=frozenset(t)
print(f1,type(f1))
s1=set(f1)
print(s1,type(s1))
print("/"*100)

# 4.dict to set
d={1:10,2:20,3:30}
print(d,type(d))
s1=set(d.items())
print(s1,type(s1))
print("/"*100)
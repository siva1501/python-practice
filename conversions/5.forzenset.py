#Frozenset
# 1.list to frozenset
l=[1,2,3,4,5,6,"siva"]
print(l,type(l))
f=frozenset(l)
print(f,type(f))
print("/"*100)

# 2. tuple to frozenset
t=(1,2,3,4,5,6,"siva")
print(t,type(t))
f=frozenset(t)
print(f,type(f))
print("/"*100)

# 3. set to frozenset
s={1,2,3,4,5,6,"siva"}
print(s,type(s))
f=frozenset(t)
print(f,type(f))
print("/"*100)

# 4.dict to frozenset
d={1:10,2:20,3:30}
print(d,type(d))
f=frozenset(d.items())
print(f,type(f))
print("/"*100)

#Dict
#list to dict
l=[("1",10),("2",20)]
print(l,type(l))
d=dict(l)
print(d,type(d))
print("/"*100)

#tuple to dict
t=(("1",10),("2",20))
print(t,type(t))
d=dict(t)
print(d,type(d))
print("/"*100)

#set to dict
s={("1",10),("2",20)}
print(s,type(s))
d=dict(s)
print(d,type(d))
print("/"*100)

#frozen set
s={("1",10),("2",20)}
f1=frozenset(s)
print(f1,type(f1))
d=dict(f1)
print(d,type(d))
print("/"*100)
#Dict
d1={}
print(d1,type(d1))
d1[1]="siva"
d1[2]="mani"
d1[3]="venkey"
d1[4]="mukesh"
print(d1,type(d1))
d2={
    "name":"siva",
    "marks":120,
    "age":25
}
print(d2,type(d2),id(d2))
print(d1[1])
print(d1,type(d1))
d1[1]="mahi"
print(d1,type(d1))
#clear()
d1={1: 'siva', 2: 'mani', 3: 'venkey', 4: 'mukesh'}
print(d1,type(d1))
d1.clear()
print(d1,type(d1))
#copy()
d1={1: 'siva', 2: 'mani', 3: 'venkey', 4: 'mukesh'}
print(d1,type(d1),id(d2))
d2=d1.copy()
print(d2,type(d2),id(d2))

#pop()
d1={1: 'siva', 2: 'mani', 3: 'venkey', 4: 'mukesh'}
print(d1,type(d1),id(d2))
d1.pop(1)
print(d1,type(d1))

#popitem()
d1={1: 'siva', 2: 'mani', 3: 'venkey', 4: 'mukesh'}
print(d1,type(d1),id(d2))
d1.popitem()
print(d1,type(d1))

#keys()
d1={1: 'siva', 2: 'mani', 3: 'venkey', 4: 'mukesh'}
print(d1,type(d1),id(d2))
print(d1.keys(),type(d1))

#values()
d1={1: 'siva', 2: 'mani', 3: 'venkey', 4: 'mukesh'}
print(d1,type(d1),id(d2))
print(d1.values(),type(d1))

#items()
d1={1: 'siva', 2: 'mani', 3: 'venkey', 4: 'mukesh'}
print(d1,type(d1),id(d2))
kv=d1.items()
print(kv,type(kv))
d1={1: 'siva', 2: 'mani', 3: 'venkey', 4: 'mukesh'}
for x in kv:
    print(x)
for k, v in kv:
    print(k,"-->",v)
print("*"*50)
for k,v in d1.items():
    print(k,"-->",v)

#uppdate()
d1={1:10,2:20,3:30}
d2={4:40,5:50,6:60}
print(d1,type(d1))
print(d2,type(d2))
d1.update(d2)
print(d1,type(d1))

#get
d1={1: 'siva', 2: 'mani', 3: 'venkey', 4: 'mukesh'}
print(d1,type(d1))
print(d1.get(1))

#zip
l1=(1,2,3,4,5)
l2=(10,20,30,40,50)
d1=dict(zip(l1,l2))
print(d1)
l1=(1,2,3,4,5)
l2=("siva","ram","raju","ramesh","mukesh")
d1=dict(zip(l1,l2))
print(d1)

##########################
d1={1: 'siva', 2: 'ram', 3: 'raju', 4: 'ramesh', 5: 'mukesh'}
print(d1,type(d1))
ksr=d1.items()
l1=list(ksr)
print(l1,type(l1))
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
print("/"*50)
d1={1: 'siva', 2: 'ram', 3: 'raju', 4: 'ramesh', 5: 'mukesh'}
print(d1,type(d1))
l1=list(d1.items())
print(l1,type(l1))
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])



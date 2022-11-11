d={1:"Sagar",2:"Siddhraj",3:"Hardik",4:"Dixit"}

print(d)
print(d[3])
d1=d.copy()
print(d1)
print(d.get(2))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(1))
print(d.popitem())
d2={10:"Sagar",20:"Dixit",30:"Jigar"}
d.update(d2)
print(d)
d[50]="Jay"
print(d)


for i in d:
    print(i," : ",d[i])

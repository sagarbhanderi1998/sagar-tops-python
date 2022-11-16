n=int(input("Enter Number : "))

x=len(str(n))

data=0
for i in str(n):
    data=data+(int(i)**x)

if data==n:
    print(n," Is Armstrong Number")
else:
    print(n," Is Not Armstrong Number")
    

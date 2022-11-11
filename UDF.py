def oddeven(n):#Nisha
    if n%2==0:
        print("even number")
    else:
        print("odd number")

def maxoftwo(a,b):#Vishal
    if a>b:
        print(a,"is max")
    else:
        print(b,"is max")
def maxofthree(a,b,c):#Kishor
    if a>b:
        if a>c:
            print(a,"is max")
        else:
            print(c,"is max")
    elif b>c:
        print(b,"is max")
    else:
        print(c,"is max")
def primenumber(a):#Dharti
    if a%2!=0:
        for i in range(3,int(a/2)+1,2):
            if a%i==0:
                print("It's Non Prime")
                break
    else:
        print("It's Prime")


def fibonacci(n):#Sagar
    a,b =0,1
    while b<n:
        print(b, end=" ")
        a,b=b, a+b
    print()

def pattern(n):#Hardik
    for i in range(1,n):
        print("*"*i)
    
    

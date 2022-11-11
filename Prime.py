n=int(input("Enter Number : "))

if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print(n," Is Not Prime")
            break
    else:
        print(n," Is Prime")
else:
    print(n," Is Not Prime")
        
            

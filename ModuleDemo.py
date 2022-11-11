import UDF

while True:

    print("*"*40)
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Prime")
    print("5. Fibonacci")
    print("6. Pattern")
    print("7. Exit")
    print("*"*40)
    
    choice=int(input("Enter Your Choice : "))
    print("*"*40)

    if choice==1:
        a1=int(input("Enter Value : "))
        UDF.oddeven(a1)
        print("*"*40)
    elif choice==2:
        a1=int(input("Enter Value : "))
        a2=int(input("Enter Value : "))
        UDF.maxoftwo(a1,a2)
        print("*"*40)
    elif choice==3:
        a1=int(input("Enter Value : "))
        a2=int(input("Enter Value : "))
        a3=int(input("Enter Value : "))
        UDF.maxofthree(a1,a2,a3)
        print("*"*40)
    elif choice==4:
        a1=int(input("Enter Value : "))
        UDF.primenumber(a1)
        print("*"*40)
    elif choice==5:
        a1=int(input("Enter Value : "))
        UDF.fibonacci(a1)
        print("*"*40)
    elif choice==6:
        a1=int(input("Enter Value : "))
        UDF.pattern(a1)
        print("*"*40)
    else:
        print("Good By")
        break
    

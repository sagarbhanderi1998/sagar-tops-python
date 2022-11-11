try:
    x=int(input("Enter Value : "))

    if x>0:
        print("Square Of ",x," Is ",x*x)
    else:
        raise Exception("There is some netowrk issue.")

except Exception as e:
    print("Exception Caught : ",e)
        

file=open("tops1.txt","w")
file.write("This is file management demo using python.")
file.close()
print("File written successfully")

print("*"*50)

file=open("tops1.txt","r")
print(file.read())
file.close()

print("*"*50)

file=open("tops1.txt","a")
file.write("\nNow this file is appended")
file.close()
print("File appended successfully")

print("*"*50)

file=open("tops1.txt","r")
print(file.read())
file.close()

print("*"*50)

file=open("tops2.txt","w+")
file.write("This is w+ mode using python.")
print(file.tell())
file.seek(10)
print(file.read())
file.close()

print("*"*50)

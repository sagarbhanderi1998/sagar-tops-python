class StaticDemo:

    center="Sg Highway"

    def student(self,name,course):
        self.name=name
        self.course=course
    def show(self):
        print("Name : ",self.name," Course : ",self.course)

s1=StaticDemo()
s2=StaticDemo()
s3=StaticDemo()

s1.student("Dixit","Python")
s2.student("Sagar","Java")
s3.student("Hardik","PHP")

s1.show()
print(s1.center)
s2.show()
print(s2.center)
s3.show()
print(s3.center)



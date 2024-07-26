# 1.Create a base class called shape withe method area that return 0 .
# create a derived class called rectangle that inherit from shape and overrides the area method to 

class shape():
    def area(self):
        return 0

class rectangle(shape):
    def __init__(self,h,w):
        self.h=h
        self.w=w
    def area(self):
        return self.h *self.w


objrec=rectangle(5,5)
print(objrec.area()) 

    

# 2.create a base class called person with constructor that takes a name as a parameter .
#  Create a derived called student that inherits from  person has constructor that takes a parameter called grade.


class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print("Name:",self.name)
        print("grade:",self.grade)

objstudent=student("Hari","A")
objstudent.display()



# 3..create a base class called vehicle with a method start that print " vehicle started" 
# create a derived class called car that inherits from vehicle and overrides the start method to print " car started”.


class vehicle():
    def start(self):
        print("vehicle started")



class car(vehicle):
    def start(self):
        print("car started")


objcar=car()
objcar.start()


# 4.create a base class called employee with properties name and salary . 
# Create a derived class called manager that inherits from employee and adds a property department .
#  Write a method in manager to display the name , salary , and department of the manager.


class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department


    def display(self):
        print("Name:",self.name)
        print("Salary",self.salary)
        print("Department:",self.department)


objmanager=manager("Hari",20000,"IT")
objmanager.display()





# 5.Create a class called animal with a sound function that prints "Animal makes sounds"
#  .create a derived class called dog that inherits from animals and overrides the sounds methods to print "dog barks " 
#  .create a another function derived class bird that inherits from animal and overrides sound method to print " birds print"


class animal():
    def sound(self):
        print("animal make sound")


class dog(animal):
    def sound(self):
        print("dog barks")
    

class bird(animal):
    def sound(self):
        print("bird print")


animal = animal()
animal.sound()

dog = dog()
dog.sound()

bird = bird()
bird.sound()
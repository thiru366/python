class goa():
    def beach(self):
        print("beach.............")
    def park(self):
        print("park..............")
hari=goa()
hari.beach()

thiru=goa()
thiru.park()




#1.Define a class Car with attributes make, model, and year.
# Create an object of this class.to print details of car use function.

class car():
    detail="car detials"
    def __init__ (self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display(self):
        print(self.detail)
        print("make:",self.make)
        print("model:",self.model)
        print("year:",self.year)
    
car1=car("Toyota","Camry","2023")
car1.display()
car2=car("Honda"," Civic","2023")
car2.display()




# 2.Create a  class called laptop. Create  a following variables and functions . 
#   		Var = price, processor, ram
# 		Create object as Lenovo, HP, Dell


class laptop():
    detial="LAPTOP"
    def __init__(self,price,processor,ram):
        self.price=price
        self.processor=processor
        self.ram=ram
    

    def display(self):
        print(self.detial)
        print("Price:",self.price)
        print("Processor:",self.processor)
        print("ram:",self.ram)

Lenovo=laptop("2,40,000","Up to Intel Core i7-1165G7","Up to 32GB LPDDR4x")
Lenovo.display()

Dell=laptop("₹2,00,000","Up to Intel Core i7-1185G7","Up to 32GB LPDDR4")
Dell.display()

Hp=laptop("₹2,00,000","Up to Intel Core i7-1165G7","Up to 16GB LPDDR4x")
Hp.display()
        

    

class student():
   detail="student"
   def __init__(self,name,age,bloodgroup):
       self.name=name
       self.age=age
       self.bloodgroup=bloodgroup

   def display(self):
       print(self.detail)
       print("name:",self.name)
       print("age:",self.age)
       print("bloodgroup:",self.bloodgroup)

obj1=student("Mukilan",17,"B+ve")
obj1.display()

obj2=student("Hari",18,"A+ve")
obj2.display()
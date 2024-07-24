# # 1.class as dad having phone as function.Class son has laptop function.
# # Create a obj for son and inherit a phone function from dad class.

class dad():
    def  phone(self):
        print("phone.....")

class son(dad):
    def laptop(self):
        print("latop.....")

objson=son()
objson.phone()




# # 2.Create a mom class having sweet function inherit from dad phone and mom sweet.


class dad():
    def  phone(self):
        print("phone.....")


class mom():
    def sweet(self):
        print("sweet.....")

class son(dad,mom):
    def laptop(self):
        print("latop.....")

objson=son()
objson.sweet()
objson.phone()


# 3.Class grandpa having phone function class dad having money function
#  class son having laptop inherit   - multilevel inheritance .


class grandpa():
    def money(self):
        print("money....")

class dad(grandpa):
    def  phone(self):
        print("phone.....")


class mom():
    def sweet(self):
        print("sweet.....")

class son(dad):
    def laptop(self):
        print("latop.....")



objson=son()
objson.phone()
objson.money()


# # 4.Class dad class having money function son1 , class son2 , class son 3, inherit dad . - hieracrchy


class dad():
    def money(self):
        print("money....")
class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass


objson1=son1()
objson1.money()
objson2=son2()
objson2.money()
objson3=son3()
objson3.money()


# 5.Class dad class having money function son1 , class son2 , class son 3, inherit dad class land having important function.
#  Inherit dad and land inherit son1.  - hybrid

class dad():
    def money(self):
        print("money....")
class land():
    def important(self):
        print("Important land")
class son1(dad,land):
    pass
class son2(dad):
    pass
class son3(dad):
    pass


objson1=son1()
objson1.money()
objson1.important()
objson2=son2()
objson2.money()
objson3=son3()
objson3.money()


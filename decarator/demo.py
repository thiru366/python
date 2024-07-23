def outer(detail):
    def inner():
        print("Thanks for entering into Ocean Academy")
        detail()
        review=input("what was though about Ocean Academy: ")
        rate=int(input("give your rating :"))
        print("your rating is ",rate,"star")
        for _ in range(rate):
            
            print("*", end="")
        
        print("\nAll the best for future endravours",a,"!")
        
   
    return inner
    



@outer 
def name():
    global a
    a=input("Enter your name:")
    print("welcome",a)
 
name()





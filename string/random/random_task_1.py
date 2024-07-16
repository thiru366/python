i=1
while i>0:
    
    import random

    fruit=["apple","mango","grapes","pineapple"]
    a=(random.choice(fruit))
    print(fruit)
    b=input("Please enter a item in the above list any one:")
    print("we guess---->",a)
    print("you guess---->",b)

    print(a==b)
    
    
    if a==b:
        print("you guess correct")
        print("if you want to play again:")
        c=input("please enter yes/no:")
        d="no"
        if c in d:
             print("thank you for playing")
             i=0
             break

        else:
            print("thank you for playing again")

        

    else:
        print("unless correct please play the game")

        
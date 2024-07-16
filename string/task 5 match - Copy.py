#match
day =int( input("Enter a day number:"))
match day: 
     case 1:
         print("sunday is a weekend")  
     case 2:
         print("Monday")     
     case 3:
         print("tuesday")
     case 4:
         print("wednesday")
     case 5:
        print("thursday")
     case 6:
        print("friday")
     case 7:
        print("saturday is a weekend")
     case __:
        print("invalid input")

# month name and number
month=str(input("Enter a month name:"))
match month:
    case "january":
        print("1")
    case  "february":
        print("2")
    case "march":
        print("3")
    case "april":
        print("4")
    case "may ":
        print("5")
    case "june":
        print("6")
    case "july":
        print("7")
    case "augest":
        print("8")
    case "september":
        print("9")
    case "october":
        print("10")
    case "november":
        print("11")
    case "december":
        print("12")
    case _:
        print("invalid input")

#day number and day name  
# #match
day =int( input("Enter a day number:"))
match day: 
     case 1:
         print("sunday")  
     case 2:
         print("Monday")     
     case 3:
         print("tuesday")
     case 4:
         print("wednesday")
     case 5:
        print("thursday")
     case 6:
        print("friday")
     case 7:
        print("saturday")
     case __:
        print("invalid input")  


# #match
a =str( input("Enter a letter:"))
match a: 
     case "a":
         print(a,"is  vowel letter")  
     case "e":
         print(a,"is  vowel letter")  
     case "i":
          print(a,"is  vowel letter")
     case "o":
        print(a,"is vowel letter")
     case "u":
        print(a,"is  vowel letter")    
     case __:
        print(a,"is not vowel letter")


a =int( input("Enter a percentage:"))
match a: 
    case a if a>=90 and a<=100 :
        print(a,"grade A")
    case a if a>=80 and a<90 :
        print(a,"grade B")
    case a if a>=75 and a<80:
        print(a,"grade C")
    case a if a>=35 and a<75:
        print(a,"grade D")
    case  a if a<35:
        print(a,"grade E")
    case _:
        print("Invalid input")



# month name and number
month=str(input("Enter a month name:"))
match month:
    case "january":
        print("January - 31 days" )
    case  "february":
        print("February - 28 or 29 days (leap year)")
    case "march":
        print("March - 31 days")
    case "april":
        print("April - 30 days")
    case "may":
        print("May - 31 days")
    case "june":
        print("June - 30 days")
    case "july":
        print("July - 31 days")
    case "augest":
        print("August - 31 days")
    case "september":
        print("September - 30 days")
    case "october":
        print("October - 31 days")
    case "november":
        print("November - 30 days")
    case "december":
        print("December - 31 days")

        
    case _:
        print("invalid input")

# #month name and season
month=str(input("Enter a month name:"))
match month.lower():
    case "january":
        print("January - Winter")
    case  "february":
        print("February - Winter")
    case "march":
        print("March - Winter to Spring (transition)")
    case "april":
        print("April - Spring")
    case "may":
        print("May - Spring")
    case "june":
        print("June - Spring to Summer (transition)")
    case "july":
        print("July - Summer")
    case "augest":
        print("August - Summer")
    case "september":
        print("September - Summer to Autumn (transition)")
    case "october":
        print("October - Autumn")
    case "november":
        print("November - Autumn")
    case "december":
        print("December - Autumn to Winter (transition)")
    case _:
        print("invalid input")
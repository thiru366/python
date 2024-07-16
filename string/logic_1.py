def party_cigar(cigars,is_weekneed):
    if is_weekneed:
        return cigars>=40
    else:
        return 40>=cigars

print(party_cigar(30,70))
print(party_cigar(80,70))




# Logic-1 > date_fashion
def get_table(you,date):
    if you<=2 or date<=2:
        return 0
    elif you>=8 or date>=8:
        return 2
    else:
        return 1
print(get_table(8,2))
print(get_table(3,7))
print(get_table(5,9))





# Logic-1 > squirrel_play

def squrile_play(temp,is_summer):
    if is_summer:
        return  60<= temp <=100
    else:
        return 60<= temp <=90

print(squrile_play(70,90))
print(squrile_play(90,90))
print(squrile_play(30,100))
print(squrile_play(60,90))




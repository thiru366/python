def hello_name(name):

       print("Hello "+ name + "!")

hello_name("Bob")



def make_abba(a,b):
       return a+b+b+a
print(make_abba("hi","bye"))



def make_tags(tag, word):
    return "<"+tag+">"+word+"</"+tag+">"
    
print(make_tags('i', 'Yay'))




def make_out_word(out, word):
    return out[:2]+word+out[2:]
    
print(make_out_word('<<>>', 'Yay'))




def extra_end(str):
    return str[-2:]*3
print(extra_end("Hello"))







def first_half(str):
    a=len(str)/2
    print(str[0:a])



first_half('WooHoo') 





def combo_string(a, b):
    if len(a)<len(b):
        return a+b+a
    else:
        return b+a+b



print(combo_string('Hello', 'hi')) 




def non_start(a, b):
    if len(a)>0:
        aa=a[1:]
        
        if len(b)>0:
           bb=b[1:]
    return aa+bb

def left2(str):
    return  str[2:]+str[0:2]




print(left2('Hello')) 

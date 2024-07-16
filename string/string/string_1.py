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




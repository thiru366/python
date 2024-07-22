
# file=open("first.txt","x")
file=open("first.txt","w")


file.write("hello")

file=open("first.txt","a")
file.write("\nPython")
file.write("\nA Powerful")
file.write("\nand")
file.write("\nVersatile Programming Language")


file.close()


file=open("first.txt","r")
# res=file.read()
# print(res)


# file1=open("second.txt","x")
file1=open("second.txt","w")

res = file.readlines()

# for i in file:
#     print(i)



for line in res:
    file1.write(line)
file.close()
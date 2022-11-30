var1=int(input("enter 1st no.-" ))
var2=int(input("enter 2nd no.-"))
print(var1+var2)
total=var1+var2
f=open("sumtotal.txt","a")
f.write(str(total))
f.close()







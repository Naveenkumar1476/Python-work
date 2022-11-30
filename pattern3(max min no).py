max=0
min=99999
for i in range(1,6):
    num=int(input('enter a no.'))
    if (num>max):
        max=num

    if num<min:
        min=num
print('maximum value is -',max)
print('minimum value is -',min)
        

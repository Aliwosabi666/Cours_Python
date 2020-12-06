a = input("Enter le nombre 1:\t")
b = input("Enter le nombre 2:\t")
c = input("Enter le nombre 3:\t")

sup = 0
if(a < b):
    sup = b

elif(b < c):
    sup = c

else:
    sup = a

print ("Max est :",sup)

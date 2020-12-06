S=0
c=0
n=0
x=0
a=int(input("range?"))

for i in range (a):
 n=float(input("note?"))
 c=int(input("coef?"))
 n=n*c
 x=x+c
S=n+S
S=S/x
if(S>=10):
   print("bravo, votre moyenne est de ", S)
else:
   print("quel dommage, votre moyenne est de ", S)

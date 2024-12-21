x=int(input("Enter first number:    "))
y=int(input("Enter second number:   "))
z=int(input("Enter third number:    "))

if x<y<z:
    n1=x
    n2=y
    n3=z

elif x<z<y:
    n1=x
    n2=z
    n3=y

elif y<x<z:
    n1=y
    n2=x
    n3=z

elif y<z<x:
    n1=y
    n2=z
    n3=x

elif z<x<y:
    n1=z
    n2=x
    n3=y

elif z<y<x:
    n1=z
    n2=y
    n3=x

else:
    print("Numbers are equal")

x,y,z=n1,n2,n3

print("The three numbers are in ascending order are: ",x,y,z)
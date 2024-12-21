#input
n1=(input("Enter number 1 ")) #takes input as string
print(type(n1))
n2=input("Enter number 2 ") #takes input as string
print(type(n2))

n3=n1+n2 #"3"+"4"="34"
print(n3)
print(type(n3))
print("      ")



n1=int(input("Enter number 1 ")) #takes input as int
print(type(n1))
n2=int(input("Enter number 2 ")) #takes input as int
print(type(n2))

n3=n1+n2 #3+4=34
print(n3)
print(type(n3))



#swapping
n1=int(input("Enter number 1 ")) #takes input as int
n2=int(input("Enter number 2 ")) #takes input as int

print("Original numbers : ",n1,n2)

n1,n2=n2,n1
print("Swapped numbers : ",n1,n2)
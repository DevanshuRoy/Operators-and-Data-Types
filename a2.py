# Multiple assignment
a,b=4,6
x=y=z=10

#implicit conversion : automatic conversion : python system

c=a+b #a(int) + b(int) = c(int)
print(type(c))


a,b=4,6.09

c=a+b #a(int) + b(float) = c(float)
print(type(c))


a,b=4.5,6.09

c=a+b #a(float) + b(float) = c(float)
print(type(c))

d=a+int(b)
#a(int) + b(float -> int) : not python system
#forceful : explicit conversion : type casting
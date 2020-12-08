import random
#NUMBERS---------------------------------------------------------------
print(2*2)
#4

print(4**2)
#16

print(3/2)
#1.5

print(3//2)
#1

print(7%2)#Modulo/Mod
""" Multiline
Comments
"""

#------------Python uses dynamic programming-------------

print("------------------------------------------------------------")

#Text Type:         str
#Numeric Types:	    int, float, complex
#Sequence Types:    list, tuple, range
#Mapping Type:	    dict
#Set Types:	    set, frozenset
#Boolean Type:	    bool
#Binary Types:	    bytes, bytearray, memoryview

my_dog=2
print(my_dog)
my_dog=["Tom","Jerry"]
print(my_dog)

#Type(int/float/etc)
a=40
print(type(a))

b=0.12
print(type(b))

c={"apple", "banana", "cherry"}
print(type(c))

d="abc"
print(type(d))

e=1j
print(type(e))



print("---------Python Strings--------")

print("--NOTE:String is immutable--------")

name="Sam is good boy"
print(name)

print('M'+name[1:])
print(name*5)

print(name.upper()+"1")

print(name.lower()+"2")

print(name.title()+"3")

print(name.upper()+"4")

print(name.capitalize()+"5")

print(name.split())

print(name.replace("good","bad"))

txt = "The rain in Spain stays mainly in the plain"
x="boy" in txt
print(x)

y="rain" in txt
print(y)

z="rain" not in txt
print(z)




print("----------------------TYPE CASTING---------------------------")

print(random.randrange(1,50))

#INT
print("INT")  
x=int("1")
y=int(4.5245)
z=int(5)
print(x)
print(y)
print(z)

#FLOAT
print("FLOAT")  
x=float("1")
y=float(4.5245)
z=float(5)
print(x)
print(y)
print(z)

#STRING
print("STRING")  
x=str("S1")
y=str(4.5245)
z=str(5)
print(x)
print(y)
print(z)

print("-----------------------------------------STRING FORMATING----------------------------------------")
'''ERROR:Traceback (most recent call last): File "./prog.py", line 2, in TypeError: Can't convert 'int' object to str implicitly

age = 36
txt = "My name is John, I am " + age
print(txt) 
'''

age = 36
txt = "My name is John, I am {}"
print(txt.format(age))

name='Chetan'
age=20
txt="My name is \'{}\' and my age is {}"
print(txt.format(name,age))








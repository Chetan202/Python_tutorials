first=input("Enter 1 no:")
second=input("Enter 2 no:")

print("The type of 1:",type(first))
print("The type of 2:",type(second))

sum=int(first)+int(second)

print("Sum is:",sum)

print('A','B','C','D',sep="->")

print("-------------------------------")

a=input("Marks: ")
a=int(a)

if a<40:
    if (a<10):
        print("LESS Than 30")
    elif (a<20) and (a>10):
        print("LESS Than 20 and Greater than 10")
    else :
        print("LESS Than 40 and Greater than 20")
else :
    print("Greater than 40")

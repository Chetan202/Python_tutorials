print("Enter the marks")
a=int(input("Python: "))
b=int(input("PHP:  "))
c=int(input("Java:  "))
d=int(input("C++:  "))
e=int(input("MAD:  "))
total=a+b+c+d+e/500
if(total<35):
    print("Grade: E")
elif(total>35 and total<45):
    print("Grade: D")
elif (total>45 and total<60):
    print("Grade: C")
elif(total>60 and total<75):
    print("Grade: B")
else:
    print("Grade: A")

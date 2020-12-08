num = int(input("Enter a Number: "))
result = 0
a = num
while num > 0:
    rem = num % 10
    result = result + rem
    num = int(num/10)
print("Sum of all digits of", a, "is: ", result)

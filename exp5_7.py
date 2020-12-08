Number = 123456789 
Reverse = 0
print("The no is: ",Number)
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
print("Reverse of entered number is = ",Reverse)  

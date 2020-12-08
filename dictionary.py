"""
1.Unorderd
2.key:value pair
3.{} 
4.No duplicate keys
"""
#-------------------------------------CREATION
dict1={1:"Geeks",2:"For",3:"Geeks"}
print(dict1)
#-------------------------------------ADDING
dict1[1]="Welcome"
dict1[2]="to"
print(dict1)
#-----------------------------------UPDATE
dict1[1]="Geeks"
dict1[2]="for"
print(dict1)
#-----------------------------------DELETE
# using pop()
print(dict1)  
dict1.pop(2) 
 
# using popitem()  
dict1.popitem() 
print(dict1) 
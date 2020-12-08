"""
1.Mutable
2.Unordered
3.No-duplicate
4.Iterable
5.([])
6.Unindexed
"""

#--------------------------------CREATION
set2=set([12,3,13,"GEEKS OF GEEKS"])
print(set2)
#--------------------------------ADD/UPDATE
#Add
set2.add((5,50))
set2.add(500)
print(set2)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Update
set2.update([90,"Shiva"])
set2.update([70])
print(set2)
#---------------------------REMOVE 
set1 = set([1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12])  
 
# using Remove() method  
set1.remove(5)  
set1.remove(6)
print(set1)  
 
# using Discard() method  
set1.discard(8)  
set1.discard(9)
print(set1)  
 
# Set using the pop() method  
set1.pop()
print(set1)  
 
# Set using clear() method  
set1.clear()
print(set1) 
    

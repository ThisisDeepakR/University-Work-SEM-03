#creating an empty list for universel set
universelset=[]
#number of elements as input for universel set
n1=int(input("enter number of elements in universel set:"))
#iterating till the range
for i in range(0,n1):
    eleu1=(input())
    universelset.append(eleu1)#adding the element to universel set
print("the universel set is",set(universelset))

#creating an empty list for set1
set1=[]
#number of elements as input for set1
n1=int(input("enter number of elements in set1:"))
#iterating till the range
for i in range(0,n1):
    ele1=(input())
    set1.append(ele1)#adding the element to set1
print("the set1 is",set(set1))
#creating an empty list for set2
set2=[]
#number of elements as input for set2
n2=(input("enter number of elements in set2:"))
#iterating till the range
for i in range(0,n2):
    ele2=int(input())
    set2.append(ele2)#adding the element to set2
print("the set2 is",set(set2))
print("the universel set is",set(universelset))
print("the set1 is",set(set1))
#union of two sets set1 and set2
union=set1+set2
print("union of two sets set1 and set2",set(union))
#intersection of two sets set1 and set2
intersection=[]
for num in set1:
    for item in set2:
        if num==item:
            intersection.append(num)
print("intersection of two sets set1 and set2 is ",set(intersection)) 
#difference of two given sets
#set1-set2
res1=[]
for value1 in set1:
    if not value1  in  set2:
        res1.append(value1)
print("diference of set1-set2 is",set(res1))
#set2-set1
res2=[]
for value2 in set2:
    if not value2  in  set1:
        res2.append(value2)
print("diference of set2-set1 is", set(res2))
#complement of set1
res3=[]
for value3 in universelset:
    if not value3  in  set1:
        res3.append(value3)
print("complement of set1 is ",set(res3))
#complement of set2
res4=[]
for value4 in universelset:
    if not value4  in  set2:
        res4.append(value4)
print("complement of set2 is ",set(res4))
print("program done by Deepak R")













    


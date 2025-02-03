mylist = ["apple" , "banana" , "cherry"]
print (mylist)
print(len(mylist))
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#acces list items

mylist = ["aplle" , "banana" , "cherry"]
print(mylist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
if "melon" in mylist:
    print ("Yes melon is in the list ")


#change list items

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
mylist[0] = "peach"
print(mylist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
mylist.insert(3,"watermelon")
print(mylist)

#add list items

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
mylist.append("orange")
print (mylist)

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
mylist.insert(0, "watermelon")
print(mylist)

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
herlist = ["pineapple" , "mango" , "papaya"]
mylist.extend(herlist)
print(mylist)

#remove list items

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
mylist.remove("apple")
print (mylist)

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
mylist.pop(1)
print(mylist)

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
mylist.pop()
print(mylist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop lists

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
for i in mylist:
    print(i)
    
mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
for i in range(len(mylist)):
    print (mylist[i])

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
i=0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

#list comprehension 

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
newlist = []

for i in mylist :
    if "a" in i:
        newlist.append(i)

print(newlist)

#sort list alphanumerically

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
mylist.sort()
print (mylist)

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
mylist.sort(reverse=True)
print(mylist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#copy lists

mylist = ["apple" , "banana" , "kiwi" , "melon" , "cherry"]
thislist=mylist
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#join lists

list1= ["a" , "b" , "c"]
list2=[1,2,3]

list3=list1+list2
print(list3)

list1= ["a" , "b" , "c"]
list2=[1,2,3]
for i in list1:
    list2.append(i)

print(list2)   

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
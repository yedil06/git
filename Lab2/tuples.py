thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple", "banana", "cherry")
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple))

thistuple = ("apple",)
print(type(thistuple))

#access tuples

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  

#update tuples  

x= ("oljk" , "anu" , "mans")
y=list(x)
y[1]="anuochki"
x=tuple(y)

print(x)

mytuple=("anu" , "oljk" , "mans")
y=list(mytuple)
y.append("edil")
mytuple=tuple(y)

print (mytuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

mytuple=("anu" , "oljk" , "mans")
y=list(mytuple)
y.remove("oljk")
mytuple=tuple(y)
print(mytuple)

#unpack tuples

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)



fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#loop tuples

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
for i in fruits:
  print(i)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
for i in range(len(fruits)):
  print (fruits[i])

#join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

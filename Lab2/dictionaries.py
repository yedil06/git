thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["year"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))



thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))

#access dict items

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) 

car["color"] = "white"

print(x)



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x)

car["year"] = 2020

print(x)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) 
car["year"] = 2020

print(x)


#change dict items

dict = {
    "name" : "Ronaldo" , 
    "birthday" : "5 February",
    "club" : "ManUnited"
}

dict["club"] = "Al Nassr"
print(dict)


dict = {
    "name" : "Ronaldo" , 
    "birthday" : "5 February",
    "club" : "ManUnited"
}

dict.update({"club":"Al Nassr"})
print(dict)


#add dict items


dict = {
    "name" : "Ronaldo" , 
    "birthday" : "5 February",
    "club" : "ManUnited"
}
dict["position"] = "forward"
print(dict)


#remove dict items

dict = {
    "name" : "Ronaldo" , 
    "birthday" : "5 February",
    "club" : "ManUnited"
}
dict.pop("birthday")
print(dict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#loop dict

dict = {
    "name" : "Ronaldo" , 
    "birthday" : "5 February",
    "club" : "ManUnited"
}
for i in dict :
    print (i)


dict = {
    "name" : "Ronaldo" , 
    "birthday" : "5 February",
    "club" : "ManUnited"
}
for i in dict:
    print(dict[i])


dict = {
    "name" : "Ronaldo" , 
    "birthday" : "5 February",
    "club" : "ManUnited"
}    
for i in dict.values():
    print(i)


dict = {
    "name" : "Ronaldo" , 
    "birthday" : "5 February",
    "club" : "ManUnited"
}    
for x,y in dict.items():
    print (x,y)   


#copy a dict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#nested dicts

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child3"]["year"])
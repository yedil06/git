import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print (x)



import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)



import re
txt = "Ronaldo is the best striker"
x = re.findall("Messi" , txt)
print (x)


import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())



import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)



import re 

txt = "Ronaldo is the best striker"
x = re.split("\s" , txt)
print (x)
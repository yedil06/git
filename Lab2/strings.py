print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


a= "Edik"
print (a[2])

for i in "Yedilkhan":
    print(i)

a="Yedilkhan"
print (len(a))

txt = "Real Madrid is the best fc in the wrld"
print ("wrld" in txt )

txt = "Real Madrid is the best fc in the wrld" 
if "wrld" in txt:
    print ("Yes , wrld is present")

txt = "Real Madrid is the best fc in the wrld"
print ("Barca" in txt)

#slicing strings

b="Yedilkhan"
print(b[2:6])

b="Yedilkhan"
print(b[:6])

b="Yedilkhan"
print(b[-5:-1])

#modify strings

a="Yedilkhan"
print(a.upper())

a="Yedilkhan"
print(a.lower())

a="Yedilkhan"
print(a.strip())

a="Yedilkhan"
print(a.replace ( "Y","n"))

a="Yedilkhan , top"
print(a.strip (","))

#concatenate strings
a="Yedil"
b="top"
c= a + b
print(c)

a="Yedil"
b="top"
c= a + " " + b
print(c)

#format strings
age = 36
txt = f"My name is John, I am {age} yo"
print(txt)

price = 300
txt =f"My phone costs {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

#escape character

txt = "We are the so-called \"Vikings\" from the north."
print(txt)


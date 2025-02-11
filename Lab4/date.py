import datetime

x = datetime.datetime.now()
print(x)



import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


import datetime

x=datetime.datetime(2023, 5 , 23)
print (x)



import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))



#EXERCISES

from datetime import datetime,timedelta

currentdate=datetime.now()
newdate = currentdate - timedelta(days=5)
print ("Date after subtracting 5 days :" , newdate.strftime("%d/%m/%Y"))





from datetime import datetime , timedelta

currentdate = datetime.now()
yesterday = currentdate - timedelta(days=1)
tomorrow = currentdate + timedelta(days=1)

print("Today :" , currentdate.strftime("%d/%m/%Y"))
print("Yesterday :" , yesterday.strftime("%d/%m/%Y"))
print("Tomorrow: ", tomorrow.strftime("%d/%m/%Y"))





from datetime import datetime

currentdate = datetime.now()

newdate = currentdate.replace(microsecond=0)

print("Date without microseconds : ", newdate)




from datetime import datetime

date1 = datetime(2024 , 10 , 14 , 12, 0 , 0)
date2 = datetime(2024 , 10 , 12 , 11 ,  50 , 0)

difference = (date1 - date2).total_seconds()

print("Difference in seconds " , difference)




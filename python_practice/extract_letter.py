#string function:
#extract lette in string
mystr="hellow world"
print(mystr[3])
#string slicing [startinclude:endexclude]
print(mystr[1:7])
#to know the length of string we will use len()
print(len(mystr))
print(mystr[0:100])
#advance extended slicing [startinclude:endexclude:stepsize(skip character)]
print(mystr[0:100:2])
#reverse string '-' it read after o -1 -2 ..
print(mystr[::-1])
print(mystr[-4:-1])
#count()
print(mystr.count("o"))
#capitalize string
print(mystr.capitalize())
#find()
print(mystr.find("low"))
#lower()
print(mystr.lower())
#title()
print(mystr.title())
#upper()
print(mystr.upper())
#Replace("type the word you reple","type the replacment")
print(mystr.replace("world","earth"))
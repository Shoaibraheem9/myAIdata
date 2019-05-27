"""dictionary data type  "{}"curly brackets
if you want to lookup any value so you will use dictionary it maps key values.
 it is key value pairs)
  syntex:
dictionary_name{"key:vale","key:value","key:value"}"""

#if you want to know the value of any key:
#dict={"shoaib":"raheem","waqas":"ismail","noman":"ibrahim"}
#print(dict)

#nested dictionary
dict={"shoaib":{"s/o":"rahemm","age":"26"},"waqas":"ismail","noman":"ibrahim"}
print(dict["shoaib"])
#if you want to know the value of any nasted key:
print(dict["shoaib"]["age"])

#to add key and pairs in dictionary:
dict["danish"]="iqbal"
print(dict)
#how to delete any key and pairs in dictionary
del dict ["danish"]
print(dict)

#if you want to make a copy of any dictionary: it is used for safe editions.
dict2=dict.copy()
del dict2 ["shoaib"]
print(dict2)

#if you want to get any valeu of any key:
print(dict.get("shoaib"))

#if you want to update any key value pairs:
dict2.update({"shoaib":{"s/o":"raheem","age":"26"}})
print(dict2)
#if you want to know all key in dictionary:
print(dict2.keys())
#if you want to know all keys of your nasted dictionary:
print(dict2["shoaib"].keys())
#if you want to know all your items in your dictionary:
print(dict2.items())
#if you want to know all your items in your nested dictionary:
print(dict2["shoaib"].items())

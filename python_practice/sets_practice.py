#set it is a collection of well defined object
#set in list



s_from_list=set([1,2,3,4])
print(s_from_list)
print(type(s_from_list))


#another way to make set:
set1=[1,2,3,4]
s_from_list=set(set1)
print(set1)
print(type(s_from_list))

#how to add elements in sets
s_from_list.add(6)
print(s_from_list)

#set doesnt written duplicate values
s_from_list.add(6)
print(s_from_list)
#it written just unique value
s_from_list.add(7)
print(s_from_list)


#made a set for set oprations
s=set()
s.add(1)
s.add(2)
print(s)

#to do set union operation:
s1=s.union({1,2,3})
print(s,s1)
#for set intersection:
s2=s.intersection({1,2,3,4})
print(s,s2)




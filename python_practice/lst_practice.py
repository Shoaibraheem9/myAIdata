#[]square brackets list data type(it is mutable means can change ,replace or append) :
cattle_feed=["palm","masoor kutta","mash kutta","chana chilka","chowker"]
print(cattle_feed)
#sort()
number=[6,10,8,4,5,1,9]
number.sort()
print(number)
#reverse()
number.reverse()
print(number)
#append() (it will add more items in your list)

#number=[]
#cattle_feed=[]

number.append(100)
cattle_feed.append("toor atti")
print(number,cattle_feed)
#insert (after this index , add this item)
number.insert(2,1001)
print(number)
#remove (it will remove an item which you want to remove)
number.remove(1001)
print(number)
#pop (it will chop off last item)
number.pop()
print(number)
#if you want to change a value of any index:
number[3]="shoaib"
print(number)

#()parentheses tuple data type (it is immutable cant change)
tp=(1,4,7,10)
print(tp)
#if you want to make a tuple of one item:
tp_one=(1,)
print(tp_one)
# a traditional way to swap the value of any variable with other variable:
a=5
b=10

#temp = a
#a = b
#b = temp
#print(a,b)

#but in python you have short way to swap values:
a,b = b,a
print(a,b)

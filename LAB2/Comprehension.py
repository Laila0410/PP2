fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# ['apple', 'banana', 'mango']
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# ['apple', 'banana', 'mango']

newlist = [x for x in range(10)]
print(newlist)
# [0,1,2,3,4,5,6,7,8,9]
newlist = [x for x in range(10) if x < 5]
print(newlist) 
# [0,1,2,3,4]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
# ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
newlist = ['hello' for x in fruits]
#['hello', 'hello', 'hello', 'hello', 'hello']
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) 
# ["apple",  "cherry", "kiwi", "mango"]

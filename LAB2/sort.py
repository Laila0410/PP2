# sort()
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# [23, 50, 65, 82, 100]
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
# ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = False)
print(thislist)
# ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# [50, 65, 23, 82, 100]
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# ['banana', 'cherry', 'Kiwi', 'Orange']

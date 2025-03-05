size_list = input("list: ")
my_list = list(map(int, size_list.split()))
times = 1
for i in my_list:
    times *= i
if(times == 1):
    print("list is true" )
else:
    print("list is false")

size_mylist=input("Enter  mylist:")
mylist=list(map(int,size_mylist.split()))
print("all True mylist:",all(mylist))
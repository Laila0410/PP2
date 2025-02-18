def square_atob(a,b):
    for i in range(a, b+1):
        yield i**2
a=int(input())
b=int(input())
num = square_atob(a,b)
for num in square_atob(a,b):
    print(num)
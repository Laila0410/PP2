def return_from0ton(n):
    for i in range(n, 0, -1):
        yield i
n = int(input())
num = return_from0ton
for num in return_from0ton:
    print(num)
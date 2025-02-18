def div_to_3_4(n):
    for i in range(0, n+1):
        if i%3 == 0 and i%4 == 0:
            yield str(i)
n = 50
for num in div_to_3_4(n):
    print(num)
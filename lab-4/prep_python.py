n=int(input())
sum=0
count=0
import random
for j in range (n):
    print(random.randint(1,30), end=" ")
if(j%2==0):
    sum+=j
else:
    count+=j
print()
print(sum, count)
# random.uniform() для вещественных чисел:
#for _ in range(5):
#    print(random.uniform(1.5, 10.5))
# random.randint() для натуральных числе:

# import random

# for _ in range(5):  # Генерируем 5 случайных чисел
#    print(random.randint(1, 100))
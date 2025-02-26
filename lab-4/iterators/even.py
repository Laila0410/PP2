def even(n):
    for i in range(0, n+1, 2):
            yield  str(i)
n = int(input())
ex = even(n)
print(", ". join(ex))

def even(n):
    for i in range(0, n+1, 2):
            yield i
n = int(input())
ex = even(n)
for num in ex : 
      print(num, end = ", ")



# str(i) — это функция, которая преобразует число i в строку.
# join() — это метод строк, который соединяет элементы
#  списка (или другого итерируемого объекта) в одну строку, используя указанное разделение.

# join я использовала без итератора что-бы написать с горизонтальном виде
# а если с итераторам то тогда можно без join
size_list = input("list: ")
my_list = list(map(int, size_list.split()))
times = 1
for i in my_list:
    times *= i
print(times)























"""
input() ждет, пока пользователь введет строку с числами например: 2 3 4
size_list теперь содержит строку: "2 3 4"

size_list.split() превращает строку "2 3 4" в список строк: ['2', '3', '4']
map(int, ...) превращает каждую строку в число: [2, 3, 4]
list(...) превращает это в обычный список: my_list = [2, 3, 4]
"""
"""
*args — принимает любое количество позиционных аргументов.
**kwargs — принимает именованные аргументы.
"""
def sum_all(*args):
    return sum(args)
print (sum_all(1,2,3,4))
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_info(name="Laila", age=18)
"""
👉 sum_all() принимает любое количество чисел, а print_info() работает со словарём аргументов
"""

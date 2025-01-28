print(10 > 9)
print(10 == 9)
print(10 < 9)
"""
True
False
False
"""
print(bool("Hello"))
print(bool(15))
""" 
True
True
"""
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

"""
Метод __len__
всегда возращает false

"""
x = 200
print(isinstance(x, int))
"""
true
isinstance — это встроенная функция в Python, которая используется для проверки,
является ли объект экземпляром определённого класса (или кортежа классов).
"""
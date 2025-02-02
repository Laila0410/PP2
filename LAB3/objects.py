class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hi,my name is {self.name}!")
p=Person("Laila", 18)
p.greet()    





# 👉 __init__() вызывается автоматически при создании объекта.    
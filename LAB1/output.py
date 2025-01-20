x = 5
y = "John"
print(x + y)
"это будет ошибкуа. Потому что int + str   будет ошибка "
#Global variables
x=10 #это значит это глобальная переменная, что оно делает оно всегда будет доступно 
def show():
    print(x) #глобальная переменная доступна 
show()

def show():
    global x    
    x=20 
modify() # оно изменяет значение глобальная переменная
print(x) 

def myfunc(x, y):
    return x + y

result = myfunc(3, 5)
print(result)  # Вывод: 8
#myfunc() — это вызов функции myfunc, который выполняет код, определённый внутри функции. 
age = 36
txt = "My name is John, I am " + age
print(txt)
# error потому что int n str не нельзя слить
# format() c этим методом мы можем слить строку и цифру str + int 
age=18
txt= f"my age is {age}"
print(txt)
# my age is 18
""" или хочешь через точку написать например {price:.2f}  """
#через что можно сделать ? переменная потом : потом .2f 2 или любая цифра 
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
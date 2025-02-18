class cat:
    """класс іші переменная емес 'поля', 'парамаетр' дейді"""
    name = None 
    age = None 
    isHappy = None
    """ это наш класс """

    """ теперь создаем объект """
    def set_data(self, name, age, isHappy):
        self.name =  name
        self.age =  age
        self.isHappy =  isHappy
    def get_data(self):
        print(self.name,":", " age-",self.age, ", Happy-", self.isHappy )


kisagul = cat()
kisagul.set_data("kisagul", 3, True)


seniora = cat()
cat2.set_data("Zhopen", 5, False)
kisagul.get_data()
seniora.get_data()
# описание всех объектов находится в одном единмтвенном месте
print(cat1.name)
print(cat2.name)
# создаем значение 
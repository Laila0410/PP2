class cat:
    """ __init__ это констуктор"""
    
    
    def __init__(self, name, age, isHappy):
        self.set_data( name, age, isHappy)
        self.get_data()

    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name 
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print(self.name,":", " age-",self.age, ", Happy-", self.isHappy )

cat1 = cat("Barsik", 3, True)
cat2 = cat("Zhopen")
cat1.get_data()
cat2.get_data()
print(cat1.name)
print(cat2.name)
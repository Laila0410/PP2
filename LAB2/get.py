# There is also a method called get() that will give you the same result:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)

# Mustang

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
# dict_keys(['brand', 'model', 'year'])

#The values() method will return a list of all the values in the dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)
 #dict_values(['Ford', 'Mustang', 1964])

 # The items() method will return each item in a dictionary, as tuples in a list.
 
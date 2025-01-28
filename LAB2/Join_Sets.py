"""
The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""
#The union() method returns a new set with all items from both sets.

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
# {'c', 2, 'a', 'b', 3, 1}
"""
The update() method inserts all items from one set into another.

The update() changes the original set, and does not return a new set.
"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# {'b', 1, 2, 3, 'c', 'a'}

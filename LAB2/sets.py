thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# {"banana", "cherry", "apple"}
 
#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#{True, 2, 'banana', 'cherry', 'apple'}


#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
# {False, True, 'cherry', 'apple', 'banana'}

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
# {'apple', 'banana', 'cherry'}

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

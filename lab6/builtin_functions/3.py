word = input()
if word == word[::-1]:
   print("polindrome")
else: 
    print("not polindrome")

# with function or no

def polindrome(word):
    if word == word[::-1]:
        return True
    else :
        return False
word = str(input("word or num: "))
print(polindrome(word))

string = input()
sum = 0
count = 0
for i in string:
    if i >= "A" and i <= "Z":
        sum += 1
    else :
        count += 1
print (sum, end = " ") 
print (count)
# with function
def sum_of_letter(string):
    sum = 0
    count = 0
    for i in string:
        if i >= "A" and i <= "Z":
            sum += 1
        else :
            count += 1
    print("upper case letter: ", sum )
    print ("lower case letter: ", count ) 
soilem = str(input())
sum_of_letter(soilem)
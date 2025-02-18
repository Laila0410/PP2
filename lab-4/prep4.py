s=input()
c1, c2 = 0, 0
ok = True
for i in range(len(s)):
    if s[i]=='(':
        c1+=1
    if s[i]==')':
        c2+=1
    if c1 < c2 :
        ok = False
if ok and c1==c2:
    print('+')
else :
    print('-') 

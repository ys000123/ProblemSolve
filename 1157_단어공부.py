word = input()
word.upper()

s=[]
for i in range(len(word)):
    s.append(word.count(word[i]))
print(s)

for i in range(len(s)):
    if s.count(s[i])==max(s):
        a=word[i]


if a.count(i)==i:
    print (a)
else :
    print('?')


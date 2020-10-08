import sys

s= list()

for i in range(9) :
    s.append(int(sys.stdin.readline().strip()))

max_num = max(s)
index = s.index(max_num)

print(max_num)
print(index +1)
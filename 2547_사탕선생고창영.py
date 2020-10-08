T=input()   #테스트 케이스의 개수
T=int(T)
print("\n")
s=list(s)
for i in range(T):
    N=input()   # 학생 수 
    N=int()
    for i in range(N):
        s[N]=input()
    if (sum(s)/N == 0) :
        print ('YES')
    else :
        print('NO')

    print("\n")
        
N=int(input('2이상의 자연수 입력 :'))
a=list(range(N+1))
a[1]=0
i=2
while i<=N/2:
    j=2
    while i*j<=N:
        a[i*j]=0
        j+=1
    i+=1
for i in range(N+1):
    if a[i]!=0: print(i,end=' ')
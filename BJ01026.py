n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
b.reverse()
sum=0
for i in range(0,n):
    sum+=a[i]*b[i]
print(sum)
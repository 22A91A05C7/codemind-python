import math
n=int(input())
lst=map(int,input().split())
lst2=map(int,input().split())
c=sum(lst)
d=sum(lst2)
if c>d:
    print(0)
else:
    print(abs(c-d))
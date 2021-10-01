import math
def distance(x1,x2,y1,y2):
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
xsus,ysus=map(int,input().split())
xdog,ydog=map(int,input().split())
n=int(input())
a=[]
f=0
while f<n:
    f+=1
    xn,yn=map(int,input().split())
    if (2*(distance(xsus,xn,ysus,yn)))<=distance(xdog,xn,ydog,yn):
        a.append(f)
if len(a)>0:
    print(a[0])
else:
    print('NO')







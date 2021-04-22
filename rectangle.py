# Problem code:RECTANGL
try:
    t= int(input())
    for tc in range(t):
        l1 = list(map(int,input().split()))
        l1.sort()
        if l1[0]==l1[1] and l1[2]==l1[3]:
            print("YES")
        else:
            print("NO")
except:
    pass


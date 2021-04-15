# Usain Bolt Record 100m in 9.58 second

try:
    t = int(input())
    for tc in range(t):
        a,b,c,d = map(float,input().split())
        t= round(100/(a*b*c*d),2)
        UsainTime = 9.58
        if t<UsainTime:
            print("Yes")
        else:
            print("No")
        
except:
    pass

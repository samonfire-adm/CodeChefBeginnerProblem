# Problem Code AMR15A
try:
    t=int(input())

    li = list(map(int,input().split()))
    even ,odd =0,0
    for tc in range(t):
        if li[tc]%2==0:
            even+=1
        else:
            odd +=1
    if even>odd:
        print("READY FOR BATTLE")
    else:
        print("NOT READY")
except:
    pass
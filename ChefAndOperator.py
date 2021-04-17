# ProgramCode CHOPRT
try:
    t =int(input())
    for tc in range(t):
        a,b = map(int,input().split())
        if a>b:
            print(">")
        elif a<b:
            print("<")
        else:
            print("=")
except:
    pass



# Input
# 10 20
# 20 10
# 10 10
# output
#   <
#   >
#   =
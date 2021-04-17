# def isRectangle(a,b,c,d):
#     if a== b==c==d:
#         return True
#     elif a==b and c==d:
#         return True
#     elif a==d and c==b:
#         return True
#     elif a==c and b==d:
#         return True
#     else:
#         return False
# try:
#     t = int(input())
#     for tc in range(t):
#         a,b,c,d = map(int,input().split())
#         if isRectangle(a,b,c,d) is True:
#             print("Yes")
#         else:
#             print("No")
# except:
#     pass
try:
    t = int(input())
    for tc in range(t):
        a,b,c,d = map(int,input().split())
        if (a==b and c==d) or (a==c and b==d) or (a==d and c==b):
            print("Yes")
        else:
            print("No")
except:
    pass

# Input
# 3
# 1 1 2 2
# 3 2 2 3
# 1 2 2 2

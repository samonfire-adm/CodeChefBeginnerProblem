# try:
#     T= int(input())
#     for tc in range(T):
#         a = int(input())
#         b= list(map(int, str(a)))
#         if 4 in b:
#             print("1")
#         else:
#             print("0")
# except:
#     pass 
try:  
    t = int(input())
    for tc in range(t):
        a = list(str(input()))
        occur = a.count("4")
        print(occur)
except:
    pass
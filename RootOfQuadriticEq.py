# Problem code :QUADROOT

from math import sqrt
try:
    a = int(input())
    b= int(input())
    c= int(input())
    print((-b +sqrt((b*b-4*a*c)))/2*a)
    print((-b -sqrt((b*b-4*a*c)))/2*a)
except:
    pass


# Sample Input
# 1
# -8
# 15
#If Give an integer N . 
# Write a program to obtain the sum of the first and last digits of this number.
# Input
# 3 
# 1234
# 124894
# 242323
try:
    t = int(input())
    for tc in range(t):
        n = int(input())
        a= [int(d) for d in str(n)]
        sum = a[0] +a[-1]
        print(sum)
except:
    pass
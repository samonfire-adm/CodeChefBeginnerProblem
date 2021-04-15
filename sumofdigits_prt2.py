try:
    T = int(input())
    for tc in range(T):
        a = int(input())
        b = [int(x) for x in str(a)]
        total = sum(b)
        print(total)
except:
    pass


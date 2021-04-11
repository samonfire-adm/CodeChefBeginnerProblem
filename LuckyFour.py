try:
    T= int(input())
    for tc in range(T):
        a = int(input())
        b= list(map(int, str(a)))
        if 4 in b:
            print("1")
        else:
            print("0")
except:
    pass 
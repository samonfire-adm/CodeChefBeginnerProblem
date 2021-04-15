try:
    t = int(input())
    for tc in range(t):
        n = int(input())
        fact = 1
        if n < 0:
            print("factorial doesn't exist for negative numbers")
        else:
            for i in range(1, n+1):
                fact = fact*i
        print(fact)
except:
    pass
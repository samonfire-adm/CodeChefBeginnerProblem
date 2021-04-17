try:
    
    a,b=map(int,input().split())
    area = a*b
    perimeter = 2*(a+b)
    if area>perimeter:
        print("Area")
        print(f"{area}")
    elif area<perimeter:
        print("Peri")
        print(f"{perimeter}")
    else:
        print("Eq")
        print(f"{area}and{perimeter}")
except:
    pass
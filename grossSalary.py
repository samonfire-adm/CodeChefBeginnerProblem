#Gross Salary = Basic Salary + HRA + DA
try:
    hra,da,ga =0,0,0
    T = int(input())
    for tc in range(T):
        a = int(input())
        if a<1500:
            hra =(a*10)/100
            da=(a*90)/100
            ga = a+hra+da
            print(ga)
        elif (a>=1500):
            hra =500
            da = (a*98)/100
            ga = a+hra+da
            print(ga)
        else:
            print("Enter The Valid Value")
except:
    pass
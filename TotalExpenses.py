# While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000.
# If the quantity and price per item are input, write a program to calculate the total expenses.
try:
    t = int(input())
    for tc in range(t):
        q,p = map(float,input().split())
        total_expenses = q*p
        if q>1000:
            discount = total_expenses*0.1
            total_expenses = total_expenses -discount
            print(total_expenses)
        else:
            print(total_expenses)
except:
    pass

# 3 
# 100 120
# 10 20
# 1200 20

            

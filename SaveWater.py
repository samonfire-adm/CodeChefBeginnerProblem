# Program Code :SAVWATER
#Problem Of Contest:-- IIT BHU

# To address the situation of Water Scarcity in Chefland, Chef has started an awareness campaign to motivate people to use
#  greywater for toilets, washing cars, gardening, and many other chores which don't
#  require the use of freshwater. These activities presently consume y liters of water every week per
#  household and Chef thinks through this campaign he can help cut down the total usage to ⌊y/2⌋.
#  Assuming x liters of water every week per household is consumed 
# at chores where using freshwater is mandatory and a total of C liters of water is available for the entire 
# Chefland having H households for a week, find whether all the households can now have sufficient water to meet their requirements.



try:
    t=int(input())
    for tc in range(t):
        H,x,y,C=map(int,input().split())
        y=y//2
        x=x+y
        H=H*x
        if H<=C:
            print("YES")
        else:
            print("NO")
except:
    pass

# Expected Input 
# 3
# 3 1 1 3
# 1 1 1 2
# 2 1 1 1
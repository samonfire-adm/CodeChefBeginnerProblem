# The Problem Code :PAWRI
try:
    t = int(input())
    for tc in range(t):
        s = str(input())
        counter = s.count("party")
        x= s.replace("party","pawri",counter)
        print(x)
except:
    pass
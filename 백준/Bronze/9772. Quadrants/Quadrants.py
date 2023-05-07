x, y = map(float, input().split())
while (x or y):
    if not (x and y):
        print("AXIS")
        
    if (x > 0 and y > 0):
        print("Q1")

    if (x < 0 and y > 0):
        print("Q2")
    
    if (x < 0 and y < 0):
        print("Q3")
    
    if (x > 0 and y < 0):
        print("Q4")
    
    x, y = map(float,input().split())

print("AXIS")

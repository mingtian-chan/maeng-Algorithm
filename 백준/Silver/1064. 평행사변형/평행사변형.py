a,b,c,d,e,f = map(int,input().split())


# if ((b-d)/(a-c) == (d-f)/(c-e)): ##  Zero division error 일어남 
#     ans = -1
    
if (a*d + c*f + e*b) - (b*c + d*e + f*a) == 0:
    ans = -1

else:
    # ab - cd 거리
    l1 = ((c-a)**2 + (d-b)**2)**(0.5)
    # ab - ef 거리
    l2 = ((e-a)**2 + (f-b)**2)**(0.5)
    # cd - ef 거리
    l3 = ((c-e)**2 + (d-f)**2)**(0.5)
    ans = 2*(max(l1,l2,l3) - min(l1,l2,l3))


print(ans)
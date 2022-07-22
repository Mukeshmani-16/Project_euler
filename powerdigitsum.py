t=s=2**1000
total=0
while s:
    r=s%10
    total+=r
    s//=10
print(total)
    

def primeornot(n):
    total=0
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0:
                break
            else:
                total+=j
    return total

n=2000000
k=primeornot(n)
print(k)
        
        
        
               

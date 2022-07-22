total=0
a,b=1,2

while b<4000000:
    if b%2==0:
        total+=b
    a,b=b,a+b

print("sum is : "+str(total))

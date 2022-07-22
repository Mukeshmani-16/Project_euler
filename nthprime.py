def primeno(num):
    primeno=[2]
    prime=2
    while len(primeno)<num:
        prime+=1
        k=0
        for i in range(2,int(prime**0.5)+2):
            if prime%i==0:
                k+=1
        if k==0:
            primeno.append(prime)
    return prime

s=primeno(10001)
print(s)

def palindrome(i):
    return str(i)==str(i)[: :-1]

maxi=0
for i in range(100,999):
    for j in range(i+1,1000):
        p=i*j
        if palindrome(p) and p>maxi:
            maxi=p

print(maxi)

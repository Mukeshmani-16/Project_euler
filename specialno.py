
x=1000
for a in range(1,x+1):
    for b in range(1,x+1):
        if a>b:
            continue
        if a+b +(a**2 +b**2)**0.5 ==x:
            print ('a: '+ str(a)+\
                  
                  'b: '+ str(b)+ \
                  'c: '+ str(int((a**2 +b**2)**0.5)))
            print (a*b*int((a**2 +b**2)**0.5))                     
        

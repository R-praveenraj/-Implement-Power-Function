def powerfunction(a,b,c):
    if b==0:
        return 1%c
    
    result=powerfunction(a,b//2,c)
    result=result*result
    if b%2==0:
        return result%c
    else:
        return result*a%c


a=int(input())
b=int(input())
c=int(input())
print(powerfunction(a,b,c))

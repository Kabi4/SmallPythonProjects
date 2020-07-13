def fact(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return n * fac(n-1)

def fact_1(n):
    y=1
    if n==0:
        y=1
    else:    
        for i in range(1,n+1):
            y=y*i
    return y

def main():
    n=int(input())
    p=fact(n)
    q=fact_1(n)
    print(p,q)
for _ in range(int(input())):
    
    def fibo_naaci(N):
        a=1
        b=1
        for i in range(N):
            yield a
            (a,b)=(b,a+b)
    def main():
        fibo_series=fibo_naaci(int(input()))
        x=0
        for i in fibo_series:
            x=x+i
        print(x)
    if __name__=='__main__':
        main()
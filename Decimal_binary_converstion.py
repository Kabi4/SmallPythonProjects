def binary_to_decimal():
    n=int(input("Enter a binary digit "))
    x=0
    for i in range(99):
        z=0
        z=n%10
        x+=z*(2**i)
        n=n//10
        if n==0:
            break
    while x!=0:
        y=0
        y=x%10
        yield y
        x=x//10
    
def decimal_to_binary():
    n=int(input("Enter a decimal digit "))
    x=0
    for i in range(99):
        z=0
        z=n%10
        x+=z*(10**i)
        n=n//10
        if n==0:
            break
    while x!=0:
        y=0
        y=x%2
        yield y
        x=x//2    
    
def ask_for_type():
    z=int(input("Press 1 for the Binary to decimal converter and 2 for Decimal to Binary Converter : "))
    if z==1:
        l=[]
        for i in binary_to_decimal():
            l.append(i)    
        for i in l[::-1]:
            print(i,end='')
    elif z==2:
        l=[]
        for i in decimal_to_binary():
            l.append(i)    
        for i in l[::-1]:
            print(i,end='')
    else:
        print("You are not suppose to answer that m@/HerF@?k3R")
        
def main():
    ask_for_type()
    
if __name__=='__main__':
    main()
        
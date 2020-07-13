def ask_for_operation():
    a,b=map(int,input().split())
    z=input("Enter the operation sign u want to operate between given two numbers:")
    if z=='+':
        return a+b
    elif z=='-':
        return a-b
    elif z=='/':
        return a/b
    elif z=='*':
        return a*b
    elif z=='**':
        return a**b
    elif z=='//':
        return a//b
    else:
        print("Every thing has limit who the fuck do u i think i am!!")

if __name__=='__main___':
    print(ask_for_operation())
    
else:
    print(ask_for_operation())
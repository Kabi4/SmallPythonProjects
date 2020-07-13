def isPrime(x):
    """
    Checks whether the given
    number x is prime or not
    """

    if x == 2:
        return True

    if x % 2 == 0:
        return False

    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True

def ask_play():
    z=input("Do you want to print next prime? Y/N: ").upper
    if z=="Y":
        
        return True
    else:
        
        return False

def prime_show():
    playing=True
    while playing==True :
        for i in range(2,99999999):
            if isPrime(i)==True:
                print(i)
                playing=ask_play()
            elif playing==False:
                break
        
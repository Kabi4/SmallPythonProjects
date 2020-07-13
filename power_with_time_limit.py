def pow(a, b):
    """
    Return a to the power of b
    """
    if(b == 0):
        return 1
    else:
        temp = pow(a, b / 2)
        if(b % 2 == 0):
            return temp * temp
        else:
            return temp * temp * a

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(pow(a, b))
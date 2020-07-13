def calPi(limit):
    decimal=limit
    counter=0
    n=22
    q=7
    while counter!=decimal+1:
            o=0    
            z=n/q
            yield int(z-o)
            if counter==0:
                yield '.'
            o=int(z)*10
            n=n*10
            z=0
            counter+=1
            if counter==decimal+1:
                break
def main():
    pi_calc=calPi(int(input()))
    i=0
    for d in pi_calc:
        print(d,end='')
        i += 1
        if i == 40:
            print(" ")
            i = 0
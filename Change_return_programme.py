for i in range(int(input())):
    N=float(input('Enter the total amount fo dollars: '))
    quater=0
    dime=0
    nickel=0
    penny=0
    while N!=0 :
        N=N*100
        quater+=N//25
        N=N%25
        dime+=N//10
        N=N%10
        nickel+=N//5
        N=N%5
        penny+=N
        print('%s Quaters %s Dime %s Nickel %s Penny'%(quater,dime,nickel,penny))
        
'''
import math

def greedy_money_exchange(denom,amount):
    i   = 0
    used= [0]*len(denom)
    while(amount>0):# go until all money gone
        # get num of that denom to use, always round down
        num     = math.floor(amount/denom[i]) 
        used[i] = num # say we've used it
        amount  = amount-num*denom[i] # set new amount
        i       = i + 1 # go to next denom
    return used
'''
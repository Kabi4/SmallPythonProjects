import random
def flip_coin():
    z=random.randint(0,1)
    return z
    
def head_tail():
    play=True
    l=[]
    while play==True:
        out=flip_coin()
        if out==1:
            l.append('H')
        else:
            l.append('T')
        print('Number of heads are: ',l.count('H'))
        print('Number of tails are: ',l.count('T'))
        print('Total Flips: ',len(l))
        s=input("Do you want to Flip again? Y/N\n").upper()
        if s=="Y":
            play=True
        elif s=="N":
            play=False
        else:
            print('Input Not Recognized!')
            play=False

head_tail()
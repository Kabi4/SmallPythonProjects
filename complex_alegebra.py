a,b=map(int,input('Enter the value of real part ').split())
c,d=map(int,input('Enter the value of complex part ').split())
z=complex(a,c)
y=complex(b,d)
s=input('Choose one of the following Operation to be done on the following colpex number: \n(1)Addition \n(2)Subtracction \n(3)Negitaion \n(4)Inversion \n(5)Multiplication \n:')
print('First complex number is: ',z)
print('Second complex number is: ',y)
if s=='1':
    print(z+y)
elif s=='2':
    print(z-y)
elif s=='3':
    print(z/y)
elif s=='4':
    print(z**-1,y**-1)
elif s=='5':
    print(z*y)
else:
    print('I am not suppose to workk on that command!! Please try again!!')

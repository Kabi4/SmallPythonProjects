def mass_convertor():
    z=input("Enter the unit you want to convert: ").capitalize()
    if z=='Kg':
        x=float(input("Enter weight in Kg "))
        y=input("Enter the unit u want to convert into: ").capitalize()
        if y=='Ounce':
            w=35.274*x
            print('%s Ounce'%(w))
            
        elif y=='Stone':
            w=0.157473*x
            print('%s Stone'%(w))
        elif y=='Pound':
            w=2.20462*x
            print('%s Pound'%(w))
        else:
            print('Use the table "HKDMDCMM" Please u fucking idiot where MM is milligram!!')
    elif z=='Ounce':
        x=float(input("Enter weight in Ounce"))
        y=input("Enter the unit u want to convert into: ").capitalize()
        if y=='Kg':
            w=0.0283*x
            print('%s Kg'%(w))
        elif y=='Stone':
            w=0.00446429*x
            print('%s Stone'%(w))
        elif y=='Pound':
            w=0.0625*x
            print('%s Pound'%(w))
        else:
            print('Use the table "HKDMDCMM" Please u fucking idiot where MM is milligram!!')
    elif z=='Pound':
        x=float(input("Enter weight in Pound"))
        y=input("Enter the unit u want to convert into: ").capitalize()
        if y=='Ounce':
            w=16*x
            print('%s Ounce'%(w))
        elif y=='Stone':
            w=0.0714*x
            print('%s Stone'%(w))
        elif y=='Kg':
            w=0.4535*x
            print('%s Kg'%(w))
        else:
            print('Use the table "HKDMDCMM" Please u fucking idiot where MM is milligram!!')
    elif z=='Stone':
        x=float(input("Enter weight in Stone"))
        y=input("Enter the unit u want to convert into: ").capitalize()
        if y=='Ounce':
            w=224*x
            print('%s Ounce'%(w))
        elif y=='Kg':
            w=6.350*x
            print('%s Kg'%(w))
        elif y=='Pound':
            w=14*x
            print('%s Pound'%(w))
        else:
            print('Use the table "HKDMDCMM" Please u fucking idiot where MM is milligram!!')
    else:
        print('Use the table "HKDMDCMM" Please u fucking idiot where MM is milligram!!')
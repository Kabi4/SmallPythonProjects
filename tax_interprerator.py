def tax_calc(n,x):
    tax_rates_all={'Hr':5,'Raj':6,'Uk':4,'Dl':6,'Up':8,'GER':5,'PAK':6,'IN':4,'USA':6,'CAN':8}
    z=n+n*(tax_rates_all[x]*0.01)
    print("Amount: %s ,Tax(in Percentage): %s,Total Amount: %s"%(n,tax_rates_all[x],z))
def tax_location(user_input):
    if user_input=='1':
        tax_rates={'Hr':5,'Raj':6,'Uk':4,'Dl':6,'Up':8}
        print('Choose Your State : ')
        for i in tax_rates:
            print(i)
        x=input('Enter Your State code: ')
        n=int(input("Enter your amount: "))
        tax_calc(n,x)
    elif user_input=='2':
        tax_rates={'GER':5,'PAK':6,'IN':4,'USA':6,'CAN':8}
        print('Choose Your Country : ')
        for i in tax_rates:
            print(i)
        x=input('Enter Your Country code: ')
        n=int(input("Enter your amount: "))
        tax_calc(n,x)
            
def main():
    n=input("Please Enter the choice for taxes: \n (1) States \n (2) Country \n ")
    tax_location(n)
main()

'''
tax_rates = {
	'State' : {
    'AZ' : .056,
    'CO' : .029,
    'MT' : 0.0,
    'NV' : .0685,
    'TX' : .0625
   },
  'Country' : {
    'CAN' : .05,
    'UK' : .2,
    'ESP' : .21,
    'GER' : .19,
    'JAP' : .08
  }
}

print ("Enter tax lookup \n \
1: Country \n \
2: State\n")

tax_lookup = int(input())
if tax_lookup == 1:
	choice = 'Country'
else:
	choice = 'State'
cost = float(input("Enter Cost: "))
rate = str(input("Select Tax Rate (%s): " % ','.join(tax_rates[choice].keys())))

print ("Cost of %.2f in %s is %.2f" % (cost, rate, float(cost + (cost * tax_rates[choice][rate]))))
'''
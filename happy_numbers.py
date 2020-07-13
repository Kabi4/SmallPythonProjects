def happy_numbers(n):
    sum=0
    p=[]      
    while True:
        for i in n:
            sum=sum+i**2
        if sum==1:
            print('Happy number')
            break
        elif sum in p:
            print('Not A happy number')
            break
        else:
            p.append(sum)
            into_array(sum)

def into_array(n):
    intarray=str(n)
    l=[]
    for i in intarray:
        l.append(int(i))
    return happy_numbers(l)
    

def main():
    x=int(input())
    return into_array(x)

'''
def get_digits(number):
	digits = []
	while number:
		digits.append(number % 10)
		number //= 10
	digits.reverse()
	return digits

def is_happy_number(number):
	previous_numbers = []
	while True:
		digits = get_digits(number)
		sum_of_squared_digits = sum(list(map(lambda x: x **2, digits)))
		if sum_of_squared_digits == 1:
			return True
		elif sum_of_squared_digits in previous_numbers:
			return False
		else:
			number = sum_of_squared_digits
			previous_numbers.append(number)	

def print_happy_number(number):
	happy_numbers = []
	count = 0
	while count < 8:
		if is_happy_number(number):
			happy_numbers.append(number)
			count += 1
		number += 1
	return happy_numbers

print(print_happy_number(int(input())))
'''
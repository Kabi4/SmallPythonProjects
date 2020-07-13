def into_a_array(n):
    array=str(n)
    taking_array=[]
    for i in array:
        taking_array.append(int(i))
    return taking_array    

def validity(n):
    array_req=into_a_array(n)
    print(array_req)
    z=sum_checks(array_req)
    lst_digit=array_req[-1]
    
    valid_sum=sum(z)
    print(valid_sum)
    if valid_sum%10==0:
        return True
    else:
        return False
    
def sum_checks(array):
    for i in range(0,len(array),2):
        
        if array[i]*2<10:
            array[i]=array[i]*2
        else:
            array[i]=sum_of_digit(array[i])
    print(array)
    return array

def sum_of_digit(n):
    n=((n*2)//10)+((n*2)%10)
    return n
    
print(validity(input("Enter CC number to validate\r\n>")))

'''
def validate(n):
	
	intArray = intToArray(n)

	if len(intArray) % 2 == 0:
		oddEven(0, intArray)
	else:
		oddEven(1, intArray)

	if sum(intArray) % 10 == 0:
		return True
	else:
		return False

def intToArray(n):
	myArray = str(n)

	intArray = []
	for x in myArray:
		intArray.append(int(x))

	return intArray
    
#Doubles and sums array values
#Odd numbers have startIndex 1
def oddEven(startIndex, intArray):
    for i in range(startIndex, len(intArray), 2):
        newDigit = intArray[i] * 2
        if newDigit < 10:
            intArray[i] = newDigit
        else:
            intArray[i] = sumOfDigits(newDigit)
            
def sumOfDigits(n):
    return (n / 10) + (n % 10)

print validate(input("Enter CC number to validate\r\n>"))
'''
costToCover = lambda w,h,ppm: w*h*ppm
print(costToCover(50,100,0.5))

"""
Find max combination of 2 numbers in a sequence - n^2
"""
def max_comb(seq):
    temp=0
    for i,n in enumerate(seq):
        for v in seq[i+1::]:
            temp=max(temp,v+n)
    return temp
print(max_comb([1,7,3,1,3,5,4]))
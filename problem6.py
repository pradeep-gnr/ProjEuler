
# find Difference between the sum of squares and the square of the sum

import sys
import os


def sum_squares(number):

    sum=0
    for each in range(1,number+1):
        sum += pow(each,2)

    return sum

def square_sum(number):
    sum =0
    for each in range(1,number+1):
        sum+=each

    return pow(sum,2)

if __name__=="__main__":
    val1 = sum_squares(100)
    val2 = square_sum(100)

    print val2-val1
        
    

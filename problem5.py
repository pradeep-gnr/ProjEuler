
# Problem 5 :-- Smallest Multiple for All numbers between 1-20

import sys
import os

def check_divisibility(number):

    is_divisible = True
    
    for each in range(1,21):
        is_divisible = is_divisible and number%each==0
        if not is_divisible:
            continue

    return is_divisible


if __name__=="__main__":

    n=1
    while n>0:
        print n
        if check_divisibility(n):
            print n
            break
        n+=1
    
  

        
        


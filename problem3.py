
# Project Euler Solutions 

import sys
import os

def check_prime(number):

    flag=False    
    i=2
    while i<number:
        if number%i==0:
            flag=True
        i+=1

    if flag:
        return False
    return True

def find_prime_fact(no):
    prime_fact_list = []

    i=2
    largest_prime_fact = None
    
    while i<no:
       if check_prime(i):
          print i  
          if no%i==0:
              largest_prime_fact = i
        
       i+=1   
    return largest_prime_fact

if __name__=="__main__":
    print max(find_prime_fact(600851475143))

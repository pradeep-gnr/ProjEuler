#Problem 4 - find the Largest palondrome for 3 digit numbers !

import sys
import os
import ipdb

def check_palindrome(number):
    """
    Checks if a Number is a Palindrome
    """
    temp = number
    no_list = []
    check_no=''
    while number>0:
        t = number%10
        check_no+=str(t)
        number = number / 10

    return temp==int(check_no)

if __name__=="__main__":

    Max = None
    seq = range(100,1000)

    for no1 in seq:
        for no2 in seq:
            number = no1 * no2
            if check_palindrome(number):
                print "Palindrome   %d" %(number)
                if number > Max:
                    Max= number                        

    print Max

    
        
        
        





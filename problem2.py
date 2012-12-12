
#Project Euler -- Problem 2

import sys

cur_no = 1
next_no =2
count = 2
print cur_no,next_no

while 1:
  temp = cur_no
  cur_no = next_no
  next_no = temp + next_no  
  if next_no%2==0:
    count+=next_no

  if next_no<4000000:
    print next_no
    continue
  else:
    break

print "COUNT  ",count

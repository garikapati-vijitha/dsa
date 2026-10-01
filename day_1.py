# link: https://www.hackerrank.com/challenges/python-print/problem
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end="")



# Link: https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return leap
    elif year %  4 == 0:
        return True
    else:
        return leap

year = int(input())
print(is_leap(year))




# Link: https://www.hackerrank.com/challenges/py-if-else/problem
#!/bin/python3

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")




# Link: https://www.hackerrank.com/challenges/python-loops/problem
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)



# Link: https://leetcode.com/problems/fizz-buzz/
class Solution:
    def fizzBuzz(self, n: int) -> list [str]:
        r = []
        for i in range(1, n+1):
            if i % 3==0 and i% 5 == 0:
                r.append("FizzBuzz")
            elif i % 3 == 0:
                r.append("Fizz")
            elif i % 5 == 0:
                r.append("Buzz")
            else:
                r.append(str(i))
        return r
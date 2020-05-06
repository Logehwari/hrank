#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    if (s.endswith('PM')):
        res=s[:-len('PM')]
        fr=s[:2]
        num=int(fr)
        if num==12:
            res1=res
        else:
            num1=12+num
            str1=str(num1)
            res1=res.replace(fr,str1,1)
        
    if (s.endswith('AM')):
        res=s[:-len('AM')]
        fr=s[:2]
        if(int(fr)==12):
            num1=00
            str1=str(num1)
            res1=res.replace(fr,str1,1)
        else:
            res1=res
    return res1
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

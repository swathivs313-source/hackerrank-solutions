#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    arr.sort()
    dict={}
    for key in arr:
        if key in dict:
            dict[key]+=1
        else:
            dict[key]=1
    max_val=0
    min_key=0
    for key in dict:
        val=dict[key]
        if val>max_val:
            max_val=val
            min_key=key      
    return min_key

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n %2 == 0:
        print('Not Weird')
        if n in range(2,5):
            print('Not Weird')
        if n in range(6,20):
            print('Weird')
        if n > 20:
            print('Not Weird')
    else:
        print('Weird')
        
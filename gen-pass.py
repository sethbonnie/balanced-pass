#!/usr/bin/env python

from random import randint
import sys

left = ['q','w','e','r','t','a','s','d','f','g','z','x','c','v','b']
right = ['y','u','i','o','p','h','j','k','l','n','m']

def printUsage():
    print("""usage: genpass [n]
n:  Number of words to concatenate. If given, must be 1 or greater.
    Defaults to 2.""")

def genpass(lwords, rwords, passes):
    result = []
    endswith = 'left' if randint(0,1) == 0 else 'right'

    llen = len(lwords)
    rlen = len(rwords)

    for i in range(passes):
        if endswith == 'left':
            result.append(rwords[randint(0,rlen)])
        elif endswith == 'right':
            result.append(lwords[randint(0,llen)])
        endswith = 'left' if result[-1][-1] in left else 'right'

    return result
    
num_passes = 2

if len(sys.argv) > 1:
    try:
        num_passes = int(sys.argv[1])
    except ValueError:
        printUsage()
        exit()

if num_passes < 1: 
    printUsage()
    exit()


with open('left-words.txt', 'r') as l, open('right-words.txt', 'r') as r:
    lwords = [word.strip() for word in l]
    rwords = [word.strip() for word in r]

    words = genpass(lwords,rwords,num_passes)

    print(', '.join(words))
    print(''.join(words))

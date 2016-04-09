'''
Created on Apr 9, 2016

@author: thanuja
'''

import countingSheepHelper

# read Input
inputFileName = '../inputs/a_countingSheep/testInput.txt';

f = open(inputFileName,'r')

lines = f.readlines()
numTests = int(lines[0])

out = countingSheepHelper.countSheep(1692)

print out
# print lines

if __name__ == '__main__':
    pass
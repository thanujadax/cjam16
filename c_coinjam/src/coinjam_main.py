'''
Created on Apr 9, 2016

@author: thanuja
'''

import coinjam
import common

# read Input
inputFileName = '../c_input.txt';

f = open(inputFileName,'r')

lines = f.readlines()
numTests = int(lines[0])
# print numTests

tfactors = common.factors(21)
print tfactors
print list(tfactors)[1]

for i in range(numTests):
    splitLine = lines[i+1].split(' ')
    N = int(splitLine[0])
    J = int(splitLine[1])

    (jamCoins, jFactors) = coinjam.getJamCoins(N, J)

if __name__ == '__main__':
    pass



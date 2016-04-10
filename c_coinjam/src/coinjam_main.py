'''
Created on Apr 9, 2016

@author: thanuja
'''

import coinjam

inputFileName = '../inputs/c_coinjam/C-large.in';
outputFileName = '../outputs/c_coinjam/C-large.out'

f = open(inputFileName,'r')
fout = open(outputFileName,'w')

lines = f.readlines()
numTests = int(lines[0])

for i in range(numTests):
    splitLine = lines[i+1].split(' ')
    N = int(splitLine[0])
    J = int(splitLine[1])
    str1 = 'Case #' + str(i+1) + ':\n'
    fout.write(str1)
    print str1
    jamCoinDict = coinjam.getJamCoins(N, J,fout)
    print 'DONE!'
    coinjam.writeDictToFile(fout,jamCoinDict,i)

if __name__ == '__main__':
    pass



'''
Created on Apr 10, 2016

@author: thanuja
'''
import fractilseHelper
inputFileName = '../inputs/d_fractiles/D-small-attempt0.in';
outputFileName = '../outputs/d_fractiles/test.out'

f = open(inputFileName,'r')
fout = open(outputFileName,'w')

lines = f.readlines()
numTests = int(lines[0])

for i in range(1,numTests+1):
    inputString = lines[i]
    inputParams = inputString.split(' ')
    K = int(inputParams[0])
    C = int(inputParams[1])
    S = int(inputParams[2])
    out = fractilseHelper.getTileSequence(K, C, S)
    str1 = 'Case #' + str(i) + ': ' + out + '\n'
    fout.write(str1)
    
f.close()
fout.close()

if __name__ == '__main__':
    pass
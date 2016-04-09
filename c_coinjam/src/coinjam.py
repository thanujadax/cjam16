'''
Created on Apr 9, 2016

@author: thanuja
'''

import common
import numpy as np
import math

def getJamCoinsBase2(N):
    """
    Calculates jam coins in base 2 for a given string length N
    First and last digits are 1
    """
    
    # variable middle part of a jam String
    maxMiddleArray = np.ones(N)  
    maxMiddleString = ''.join(['%s' % i for i in maxMiddleArray.astype(int)])
    maxNum = int(maxMiddleString)
    
    jamCoinsDict = {}
    
    for i in range(0,maxNum+1):
        
        middleBinString = bin(i).split('b')[1]
        jamString = '1' + middleBinString + '1'
        decNumber = int(middleBinString,2)
        
        factorSet = common.factors(decNumber)
        if(len(factorSet)>1):
            jamCoinsDict[jamString] = list(factorSet)[1]
    
    return jamCoinsDict
        

def getJamCoins(N,J):
    
    """
    N - number of bits in the jamcoin. First bit and last bit are always 1
    J - number of jamcoins required
    """
    
    bases = range(2,11)
    
    jamCoins = []
    jFactors = []
    

    
    # first look for potential jam coins starting from base 2. also store one factor
    # then for these strings, check if they are still jamcoins for other bases 3,4, etc.
    # if they are not remove them from the dict

    jamCoinsDict = getJamCoinsBase2(N)
    
    common.printDictionary(jamCoinsDict)
    
    return jamCoins, jFactors


        
    

    
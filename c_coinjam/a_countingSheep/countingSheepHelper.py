'''
Created on Apr 9, 2016

@author: thanuja
'''
# import numpy as np

def intersectLists(a, b):
    """
    Returns the intersection of lists a and b
    """
    return list(set(a) & set(b))

def printDictionary(dictIn):
    for x in dictIn:
        valueOfKey = dictIn.get(x)
        str1 = str(x) + " : " + str(valueOfKey)
        print str1
        
def getKeyForValue(dictIn,val):
    outputKeys = []
    for k,v in dictIn.iteritems():
        if v == val :
            outputKeys.append(k)
    return outputKeys

def updateDictWithDigitsSeen(digitsDict,digitsSeenList):
    """
    update the dictionary{digit:isSeen}
    """
    if(not digitsSeenList):
        for k in digitsSeenList:
            digitsDict[k] = 1
    return digitsDict

def countSheep(N):
    """
    Starting from n, up to which number N should we go to see all digits 0-9 at least once
    N is returned. If it's not plausible, 0 is returned
    """
    if(N==0):
        return 0
    else:
        # digitsList = range(10)
        # zeroValues = np.zeros(10)
        #digitsDict = {key: None for key in digitsList}
        # digitsDict = dict.fromkeys(digitsList,0)
        # printDictionary(digitsDict)
        # unseenDigitsList = getKeyForValue(digitsDict, 0)
        unseenDigitsList = range(10)
        k = 1        
        while (unseenDigitsList):
            n = k * N
            print n
            nDigitList = list(int(d) for d in str(n))
            digitsSeenList = intersectLists(unseenDigitsList, nDigitList)
            # digitsDict = updateDictWithDigitsSeen(digitsDict,digitsSeenList)
            newUnseenDigitsList = [d for d in unseenDigitsList if d not in digitsSeenList]
            unseenDigitsList = newUnseenDigitsList
            k = k+1
        
    return n
    
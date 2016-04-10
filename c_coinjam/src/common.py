'''
Created on Apr 9, 2016

@author: thanuja
'''

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
def printDictionary(cars):
    for x in cars:
        print (x)
    
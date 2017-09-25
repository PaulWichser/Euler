# -*- coding: utf-8 -*-

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def ispalendrome(num):
    if isinstance(num, int):
        numlist = list(str(num))
        i = 0
#        print len(numlist)
        while i < (len(numlist)/2):
#            print i
            if numlist[i] != numlist[0 - (i + 1)]:
                return 0
            i += 1
        return 1
    else:
        return 0

palendromes = [0]   #must prefill list for max(list) to work
for i in range (100,1000):
    for j in range (i,1000):
        k = i*j
        if k > max(palendromes) and ispalendrome(k):
            palendromes.append(k)
            f1 = i 
            f2 = j

print "\nThe largest palendrome made from the product of two 3-digit numbers is %d," % (max(palendromes))
print "which is made by %d * %d.\n" % (f1, f2)

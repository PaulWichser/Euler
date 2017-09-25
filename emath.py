# -*- coding: utf-8 -*-

# Math functions I've used while solving Euler problems that I'd like to use again

def isfactor(num,fac):  #checks whether fac is a factor of num
    if not num % fac:
        return 1
    else:
        return 0

def isprime(num,primelist): #checks whether num is a prime number. Pass a list of known primes to primelist to speed up
    #TODO: develop a way for isprime to accept empty or full prime number lists. Currently only works with [2]

    # if not primelist:
    #     i = 3
    #     if not num % 2:
    #         primelist.append(2)
    #     while i*i <= num:
    #         if not num % i:
    #             primelist.append(i)
    #             if isprime(num,primelist):
    #                 return 1
    #             else:
    #                 return 0
    if not isinstance(num, int):
        return 0
    elif num == any(primelist):
        return 1
    else:
        for i in range (0 , len(primelist)):
            if not num % primelist[i]:
                return 0
        return 1

def ispalendrome(num):  #checks whether int num is a palendrome
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

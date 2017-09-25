# -*- coding: utf-8 -*-

# Math functions I've used while solving Euler problems

def isfactor(num,fac):  #checks whether fac is a factor of num
    if not num % fac:
        return 1
    else:
        return 0

def isprime(num,primelist): #checks whether num is a prime number. Pass a list of known primes to primelist to speed up
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

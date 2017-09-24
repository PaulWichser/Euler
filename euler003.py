#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#NOTE: This calculation takes less than a second without testing feedback

#TODO: develop a way for isprime to accept empty or full prime number lists. Currently only works with [2]

import time

t = time.clock()

n = 600851475143
bigprime = 0
#primes = [2,3,5,7,11,13]
primes = [2]        #seeds the isprime function with a basic prime list. See TODO
i = 3

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
#if not n % 2:
#    primes.append(2)
while i*i <= n:
    # print "i = %d   time (s): %f" % (i,time.clock()-t)
    # print primes
    # print "bigprime = %d" % (bigprime)
    if isfactor(n,i):
        if isprime(i,primes):
            primes.append(i)
            bigprime = primes[-1]
    i += 2

print "\nThe largest prime factor of %d is %d\n" % (n,bigprime)
print primes
print "\nTime to calculate: %f seconds\n" % (time.clock() - t)

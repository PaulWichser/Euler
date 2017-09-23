#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import time

t = time.clock()

n = 600851475143
bigprime = 0
i = 1

def isfactor(num,fac):  #checks whether fac is a factor of num
    if not num % fac:
        return 1
    else:
        return 0

def isprime(num):
    if not isinstance(num, int):
        return 0
    elif num == 2:
        return 1
    elif not num % 2:
        return 0
    else:
        for i in xrange (2 , num/2+1):
            if not num % i:
                return 0
        return 1

while i <= n/2:
    print "i = %d   time (s): %f" % (i,time.clock()-t)
    if isfactor(n,i):
        if isprime(i):
            bigprime = i
    i += 2

print "\nThe largest prime factor of %d is %d" % (n,bigprime)
print "\nTime to calculate (in seconds): %f" % (time.clock() - t)

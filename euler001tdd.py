def div_by_three(n):
    return not n % 3

def div_by_five(n):
    return not n % 5

def div_by_either(n):
    return div_by_three(n) or div_by_five(n)

def total(n):
    a = 0
    for i in range (1,n):
        if div_by_either(i):
            a += i
    return a

print div_by_three(3) == 1
print div_by_five(5) == 1
print div_by_either(3)
print div_by_either(5)
print div_by_either(15)
print not div_by_either(7)
print total(10) == 23
print total(1000)

from math import sqrt,floor
def isprime(n):
    if n ==1:
        return False
    for i in range(2,floor(sqrt(n)+1)):
        if n==2:
            return True
        if n%i==0:
            return False#
    return True
###
#
# Euler
#
# coprime corrected
#
# copyright 2014, Lewis Alexander Morrow
# all rights reserved
#
# permission is hereby granted for use of this work for 
# educational purposes within Olin College of Engineering, Needham, MA
#
from primetools import primetools
from fractions import gcd

class Euler(primetools):
    
   
    """ 
Introduction to Euler's totient function, also called  (phi).

 φ(d) To compute the totient of d, count the rational numbers n/d
    in the domain 1/d to d/d that are not in lowest terms.
    For φ(4) we consider 1/4, 2/4, 3/4 and 4/4.  2/4 and 4/4 can be
    can be reduced 1/2 and 1; The two rational numbers 1/4 and 3/4 cannot
    be reduced,  so the totient of 4 is 2.  The totient of a prime p is p-1,
    since all of the rational numbers less than p are irreducible.  For example,
    1/5, 2/5, 3/5, 4/5 are irreducible, so φ(5) is 4.
    
    We provide two Python algorithms for φ(d): totient_by_gcd and totient_by_coprimes.

  
  
totient_by_coprimes(d)

    If n and d are coprime, n/d can be reduced. 
    
    For example, coprime(9,12) can be written coprime(3*3,3*2*2).  Clearly,
    the common prime factor 3 can be removed, making 9/12 equivalent to 3/4.
    
totient_by_gcd(d)

    If 1 != gcd(n,d), then n/d can be reduced.
    For example, gcd(9,12) is 3, so 9/12 can be reduced.

Personal note: I've always found gcd algorithm to be a bit murky.
It seems easier and more obvious to state reducability
of a fraction as a question of whether the denominator and numerator have a
common factor (i.e., cofactor(n,d) == True)

The two algorithms are below.  Let me know which one you find easiest to remember.
By the way, Python 3 supports Unicode identifiers.


"""
    def __init__(self,*T,**D):
        print("{}.__init__({},{})".format(self,T,D))
        primetools.__init__(self,*T,**D)
        
    def totient(self,d):
        return self.totient_by_gcd(d) or self.totient_by_coprime(d) 
  

        
    def totient_by_gcd(self,d):
        return len([n for n in range(1,d+1) if 1 == gcd(n,d)])
    
    def totient_by_coprime(self,d):
        return 1+len([n for n in range(2,d+1) if self.coprime(n,d)])

    # Notes:

    # coprime(n,d) is one of the methods in primetools; be sure to
    # read primetools to discover how comprime(1,2) works. 
    

    
if __name__ == "__main__":
    print ("Unit tests for module euler")
    eu = Euler()
    
    def test(fn,val):
        print ("{}({}) == {}".format("totient",val,fn(val)))
    test(eu.totient_by_gcd,7)
    test(eu.totient_by_coprime,7)
    test(eu.totient,7)
    test(eu.totient_by_gcd,4)
    test(eu.totient_by_coprime,4)
    test(eu.totient,4)
    test(eu.totient_by_gcd,1)
    test(eu.totient_by_coprime,1)
    test(eu.totient,1)
    
    

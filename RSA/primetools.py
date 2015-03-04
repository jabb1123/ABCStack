#
# primetools - functions of primes with cache
#
# copyright 2014, Lewis Alexander Morrow
# all rights reserved
#
# permission is hereby granted for use of this module for 
# educational purposes within Olin College of Engineering, Needham, MA
#
class primetools:
    
    def __init__(self):  # in the following, a "known prime" is an int
                        # for which prime(x) has returned True in the
                        # history of this instance of primetools
        print ("init primetools")  
        self.dp =[2,3]  # dense primes (i.e. a sorted list of all primes <= lkdp)
        self.lkdp = 3   # last known dp
        self.sp=set()   # sparse primes (i.e., set of known primes > lkdp)
        
        reduce = __import__("functools").reduce
        mul    = __import__("operator").mul
        self.prod = lambda X:reduce(mul,X)
        self.gcd    = lambda X:__import__("fractions").gcd(X)
                
    def prime(self,X):
        """ Returns True if X is a prime"""
        
        if X < 2:
            raise ValueError("domain error: X<2")
        if 2 <= X <= self.lkdp:
            return X in self.dp
        if X in self.sp:
            return True
        if not self.firstdiv(X):
            self.sp.add(X)
            return True
        return False 
    
    def firstdiv(self,X):
        """
Returns empty list or singleton list [d] where d is first prime divisor of X
A prime divisor of X is a prime p <= int(X**.5) 
        """
        if X < 2: 
            raise ValueError("domain error: X<2")
        if X in self.dp or X in self.sp:
            return []
        for i in self.ple(int(X**.5)):
            if not X % i: # "not X % i" is equivalent to "i divides X evenly"
                return [i]
        return []

    def ple(self,x):
        """ generates primes p for which 2 <= p <= x  """
        for i in self.dp:  # initial conditions: self.dp = [2,3]
            if i > x:
                raise StopIteration
            yield i
            
        for i in range(self.lkdp+2,x+1,2):  # future: ignore 5's
            if not self.firstdiv(i):
                self.dp.append(i)
                self.lkdp = i
                if i in self.sp:
                    self.sp.remove(i)
                yield i
                
        raise StopIteration

        self.pbe = self.ple  # primes below or equal to is more natural-number-like terminology
        
    def factors(self, X):
        """ Returns a list of primes whose product is X """
        return (lambda fd: [X] if not fd else fd + self.factors(X // fd[0])) (self.firstdiv(X))

    def factorset(self,x):
        return {f for f in self.factors(x)}

    def cofactors(self,x,y):
        return self.factorset(x) & self.factorset(y)

    def coprime(self,x,y):
        return x == 1 or y == 1 or not bool( self.cofactors(x,y))


if __name__ == "__main__":
    from sys import version
    print ("Python version {}".format(version))
    pyver = 2 if version.startswith("2.") else 3
    if pyver == 2:        
        print ("Unit tests for primetools".format(version))
    else:
        print ("Unit tests for module {}".format(version,__file__))
    pt = primetools()
    print("primes in range(2,102) == ",[p for p in range(2,102) if pt.prime(p)])
    print("primes in pt.ple(101)  == ",[p for p in pt.ple(101)])
    bignum = 1439874169812
    print("bignum = ",bignum)
    print("factors(bignum) ==",pt.factors(bignum))
    print("factorset(bignum) ==",pt.factorset(bignum))
    print("cofactors(bignum,2) ==",pt.cofactors(bignum,2))
    print("coprime(bignum,2) == ",pt.coprime(bignum,2))
    print("coprime(2,4) == ",pt.coprime(2,4))
    print("coprime(3,7) == ",pt.coprime(3,7))
    print("coprime(1,3) == ",pt.coprime(1,3))
    print("coprime(1,1) == ",pt.coprime(1,1))


    



    

    
    



    

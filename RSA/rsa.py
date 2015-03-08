#
# RSA
#
# copyright 2014 Lewis Alexander Morrow
# all rights reserved
#
# permission is hereby granted for use of this work for 
# educational purposes within Olin College of Engineering, Needham, MA
#
#
from fractions import gcd
from itertools import count
import modulararithmetic as Modular
import euler as Euler
__doc__ = """

 

This Python package provides an implementation of the RSA encryption algorithm
intended to introduce it and explain its operation.   Its intent is to
show the use of Python as a notation for simplifying the description of
the algorithms used in the current computer networking.

This Python package provides an implementation of RSA in Python. 

Implementation Architecture

The RSA package has the following modules and class hierarchy.

   * module: primetools
   
            class Primetools:

               A collection of methods for working with primes
               Provides an iterator that yields primes in order
               Its primary goal is to be both easily understood
               and relatively efficient.

     
    * module: euler

         class Euler(Fermat):

               While the RSA algorithm is the practical basis for
               most Internet security, the totient function is the
               theoretic basis for RSA.  The totient provides the
               basis for combining modular arithmetic classes for
               different modula.  Its value to RSA is a proof
               about a property of modular arithmetic that speeds up
               modular division and exponentiation significantly if the
               prime factors of the modulus are know.

               This module provides a straightforward introduction
               to the totient function and two implementations of
               totient(n).

               
               1. totient_by_gcd(d) is based on Euclid's gcd(a,b)

               2. totient_by_coprime(d) is base on the method
               Primetools.coprime(a,b)

               The reasons for providing two methods for totient are
               covered in the module.

               It then covers Fermat's little theorem
               based on the totient, and some of Euler's work.


    * module: modulararithmetic

        class Modular_Arithmetic(Euler):

            Implements modular arithmetic for a given modulus.

                Modular_Arithmetic It implements the following Modular Arithmetic Operations:
                
                a+b  a-b  a*b  a//b  a**b    -b  ~b   repr str int

            def modular(modulus):  
            
                A simple class factory for the Modular_Arithmetic class
                Separates specification of a modulus for modular arithmetic
                operations other modular arithmetic functions. See examples.
                

   
"""       


class RSA(Euler.Euler):
    """ RSA Encryption algorithm per Wikipedia - 1 April 2014 """
    def __init__(self,*T,**D): # set level 0 assumptions
        Euler.Euler.__init__(self,*T,**D)
        

    def from_message_bit_length(self,message_bit_length=8,opt=0):
        """Create a pair of RSA classes for a given message bit length"""

        startp == 2**(1+message_bit_length//2)
        # the bitlengths of p and q should each be about 1/2 the message bitlength
                                                  # notes: 1. the starting point for the search needs to be randomized
                                                  #        2. the current search for a suitable prime pair needs to be
                                                  #           changed to a search for a suitable pseudo-prime pair
                                                  #        3. (2.) requires a pseudo-prime generator
                                                  #        4. we will need to increase the specification msg_bit_length
                                                  #           to provide room for extra bits used for 
                                                  #           pre-processing prior to RSA modular exponentiation
                                                  #        5. RSA messages are often used to exchange keys for
                                                  #           symmetric encryption algorithms
                                                  
        
        for p in count(startp): # to be randomized
            if self.prime(p): 
                for q in count(p+2):  # to be randomized
                    if self.prime(q):
                        for e in self.ple(100): # to be randomizedd
                            if not self.coprime(e,self.totient(p)*self.totient(q)):
                                return from_given_pqe(p,q,e,opt=opt)

    def from_given_pqe(self,p,q,e,opt=0):
        """Create an pair of RSA classes from a given p,q,e triple"""       
        print("{}.from_given_pqe(p={}, q={}, e={}, opt={})".format(self,p,q,e,opt))
##        print(totient(p*q) = {},\n gcd(e,totpq)={}".format(
##              self.totient(p*q),
##              gcd(e,self.totient(p*q))
##              ))
        self.private = RSA_private(p,q,e,opt=opt)
        self.public  = RSA_public(p*q,e) 
        return(self.public)
    
    def message_bit_length(self):
        return self._message_bit_length


    def loopback(self,cleartext):
        "loopback test of RSA encryption. cleartext is an integer"
        cyphertext = self.public.encrypt(cleartext)
        received   = self.private.decrypt(cyphertext)
        
        return """
Loopback test of RSA encryption and decryption
cleartext entered      = {}
cyphertext transmitted = {}
cleartext received     = {}
        """.format(cleartext,cyphertext,received)
    pass
    
                                
class RSA_public(Euler.Euler):
    """
RSA methods for hosts with public key = (pq,e)

encrypt,
  which encrypts a message which can only be decoded by the
  decrypt method of the same instance of an RSA object.

authenticate,
  which can validate a signature created which could only have been created
  by the sign method of the RSA_private class

The RSA_public class is provided with the RSA public key (pq,e) when it is
instantiated.

pq is the product of p and q.  e is the encryption exponent.

The RSA_public key class is not provided with the primes p and q.  The
RSA_private class is provided with p and q.  This is the only difference
between the two methods.
This means it does not have the factorization of the modulus pq into two primes.
Consequently, the RSA_public class does cannot calculate the totient
of p or that of q, and therefore does not know the totient of pq.
In order to decrypt the message, it must know these things.

The fundamental question of whether RSA encryption can be broken is this:
long would it take an attacker to factor pq into p and q, create to totient
of pq and therefore be able to calculate the decryption key d,
the multiplicative inverse of (e mod pq).

The answer to "how long it would take an attacker to factor pq" is therefore
the entire basis for RSA encryption.  How hard is it to do this?
encrypt: converts cleartext to RSA cyphertext for cleartext and signature authentication given cleartext
for Olin spring semester Computer Networks class
    """
    def __init__(self,pq,e,*T,**D):
        Euler.Euler.__init__(self,*T,**D)
        
        """Instantiate instance of RSA public key class with public key
(pq,e).  The methods available in the public key class are:


    """
        print("{}.__init__(pq={},e={},{},{})".format(self,pq,e,T,D))

        self.modpq = Modular.mod(pq) # create a modular arithmetic class for
                                     # modulus pq
        self.e = self.modpq(e)       # create an instance of that class
        
    def encrypt(self,cleartext):
        """
Encrypt cleartext to be sent

Encrypt the integer "cleartext"  with public key (pq,e) provided
when this object was instantiated from the RSA_public class.

The RSA public key is the tuple (pq,e) where pq is the produce of primes p and q
and e is an natural number relatively prime to totient(pq)

The user of the methods in RSA_public does not have knowledge of p, q, or totient(p*q),
which is totient(p)*totient(q) or, since p and q are prime, (p-1)*(q-1)

As can be seen in the method code, the encryption algorithm is simply this:

         (cleartext**e) % pq

         """
        
        if type(cleartext) is not int:
            raise TypeError("Cleartext must be int")
        
        self.cleartext = self.modpq(cleartext)  # convert the message to an
                                                # instance of the modulararithmetic class
                                                

        if int(self.cleartext) != cleartext:    # if "modpq" class initialization truncated
                                                # the message, complain and quit
            raise ValueError("Message too long")
        
        # Encryption -- note that the operation ** is performed modulo pq
        # because cleartext and e are instances of modulararithmetic 

        self.cyphertext = self.cleartext**self.e  # modulo pq

        # there you go!

        return int(self.cyphertext)

    def authenticate(self,receivedtext,signature):
        """Authenticate a signature.

(The hash algorithm is normally specified by a field in a certificate object)
        """
        return self.encrypt(signature) == hash(receivedtext)
        
class RSA_private(Euler.Euler):
    """
Private Key instance: decryption of received cybertext and signing of cleartext to be sent"
    """
    def __init__(self,p,q,e,opt=0,*T,**D):
        print("{}.__init__({},{}.{},{},{},{}".format(self,p,q,e,opt,T,D))
        Euler.Euler.__init__(self,*T,**D)
        """
Initialize private key operations by computing the decryption key and
choosing a decryption algorithm.

Note that the factorization of pq into p and q is
known to the private key instance but not the matching public key instance.

opt=1 chooses the Chinese Remainder Theorem.
opt=0 chooses simple exponentiation."""

        totient_p = self.totient(p)
        totient_q = self.totient(q)
        totient_pq = totient_p*totient_q
        print("totient ({} * {}) == {}".format(totient_p,totient_q,totient_pq))
        mod_totient_pq  = Modular.mod(self.totient(p)*self.totient(q))
    
        dmodpq = ~mod_totient_pq(e)  # d is the int value of
                                     # (1/e) mod (totient(p*q))

        print("~mod_totient_pq({}) == {}".format(e,repr(dmodpq)))

        d=int(dmodpq)
                                     
        self.modpq = Modular.mod(p*q)# modpq is a modular arithmetic space

        self.decrypt = self.simple_decrypt_init(d) if opt==0 else self.crt_decrypt_init(p,q,e,d)
                                     #choose the decryption algorithm based on the

                                     # opt field.
                                     # opt=0 - not optimized
                                     # opt=1 - the Chinese Remainder Theorem                                                 
                                                                                        
    def simple_decrypt_init(self,d):
    
        self.modpq_d = self.modpq(d)

        return self.simple_decrypt
        
    def simple_decrypt(self,cybertext):

        return int(self.modpq(cybertext) ** self.modpq_d)

  
    def crt_decrypt_init(self,p,q,e,d):
        """decryption requires factored primes (p and q)"""

        # precompute values used during decryption
        
        self.tp_d   = d % self.totient(p)  # note that message bit_length > totient(p).bit_length()
        self.tq_d   = d % self.totient(q)
        
        self.modp = Modular.mod(p)
        self.modp_q_inv  = ~self.modp(q)   # this requires thought - it is the multiplicative inverse of q % p

        self.modq = Modular.mod(q)
        self.q  = q

        #print("setup values self.tp_d:{}, self.tq_d, self.modp_q_inv: {}".format(
        #    self.tp_d,                    self.tq_d, self.modp_q_inv))

        return self.crt_decrypt

    
    def crt_decrypt(self,received_cyphertext):

        ct_p = self.modp(received_cyphertext) ** self.modp(self.tp_d)
        ct_q = self.modq(received_cyphertext) ** self.modq(self.tq_d)
        modp_ct_q = self.modp(int(ct_q))
        h =    self.modp_q_inv * (ct_p - modp_ct_q)

        #print("values:  ct_p:{}, ct_q:{}, modp_ct_q:{}, h:{}, self.q:{}".format(
        #    ct_p,                ct_q,    modp_ct_q,    h,    self.q))

        return int(ct_q) + int(h) * self.q       
            
    def decrypt(self,received_cyphertext):
        """ this is a placeholder that is replaced by the selected xx_decrypt_init method"""
        raise NotImplemented("should not happen")

    def sign(self,cleartext_to_be_sent):
        return crt_decrypt(hash(cleartext_to_be_sent))
    

if __name__ == "__main__":
    print ("Unit tests for module {}".format(__file__))
    rsa = RSA()
    rsa.from_given_pqe(61,53,17,opt=0)
    print(rsa.loopback(65))
    rsa.from_given_pqe(61,53,17,opt=1)
    print(rsa.loopback(65))
    print(rsa.loopback(128))
    print(rsa.loopback(1))
    print(rsa.loopback(2))
    print(rsa.loopback(3000))

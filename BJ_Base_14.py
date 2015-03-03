#
## Transforms
#

# When a thing we depend upon is enormous, complicated and broken there
# is in some people a desire to make it small, simple and elegant.
# Computing has only been around for 70 years, a single person's
# lifetime.  Twenty years after the ENIAC, in 1961, a farmer from
# Alberta graduated from Harvard.  He had enlisted in the army during
# WOrld War II, and, when he produced an astonshing mark in
# mathematics had been assigned to the Canadian air force to be
# trained as a navigator.  He said that mathematics became real rather than
# abstract to him when he realized as a navigator that the point of
# no return for an airplane was not approaching when you saw that
# you had used almost half the fuel.
#
# This person, Ken Iverson, invented a new notation for mathematics.
# His idea was that we could use computers not as replacements for
# humans -- as when the ENIAC was used to develop ballistics tables --
# but as the basis for a new mathematics.
#
# When he got his PhD at Harvard in applied mathematics he was hired by
# IBM to create a formal model of a computing system using his new
# notation.  That resulting formal model was published in the
# IBM Journal of Research and Development in 1965.  It became
# the basis for the development of the IBM/360 computer series
# which had as its goal the creation of a computer architecture
# that protected customers investments in software by providing a
# standard architecture that was small, simple and elegant enough
# to be printed in ten pages.  The problem with the ten pages is that
# they were written in a non-familiar notation.   The notation
# was a new form of mathematics.
#
# Ken and his colleagues who had created the formal model of the
# IBM/360 realized that if they were to succeed in having the
# clearly useful notation understood, they would have to start teaching
# it to students.  IBM was at the time trying to develop a computer
# for education, the IBM 1500.  Ken hired a collection of bright PhDs
# and set them to work creating a version of his notation for the
# 1500.  The work was helped by early attempts to implement the notation
# on the IBM 7094, the largest scientific computer at that time.
# The 7090 was the computer MIT had employed to create the
# Conversational Time Sharing System the first virtual computing
# environment. The 1500 was intended to be IBM's smallest computing
# system, to be inexpensive enough to be sold to secondary schools
# rather than research universities.
#
# The team successfully completed the 1500 system, but the problem was
# that it was not selling well enough to have an impact on teaching.
# They turned to the IBM/360.  They convinced IBM Reseach to fund a
# research lab that was a small IT department wholly separate from the
# large IBM Research Computing Department. They furthermore asked to
# be freed from any requirements to use IBM's standard 360 operating systems.
# Their goal was to a timesharing system based on Iverson's notation
# that would be as inexpensive as a 1500 on a per-seat basis by building
# if from the IBM/360 hardware up.  The decision was very unpopular with
# the people who ran the Research Computing Department and the
# people building IBM's official timesharing system, called TSS.
#
# The result was APL\360.  The "\" is an APL operator symbol named
# expand.  APL\360 was the APL expansion of the System 360.  APL\360
# was an operating system, a timesharing system, and a new language.
# It could support well over fifty students on a Model 50, which the
# team had selected because it was IBM's workhorse replacement for
# all of the business computers.  The interpreter for APL\360 fit in
# 70 kilobytes.  The workspace size was 36 kilobytes.  Yet is was
# possible to do real work on the system.

# It was, however, small, simple, and elegant.
#
# How elegant was hard to imagine.  IBM had hired Charles Eames to
# design a printing element - or typeball -- used on IBM Typewrites
# to provide replaceable character sets for different langauges and
# for mathematics.  Eames used his designer's eye to create a
# typeface for APL.  There was only one case, italic upper case.
# Numbers were not italic.  It was thus possible to determine at a glance
# whether 'l' was the number one or an L.  The typeface was carefully
# positioned so that many of Iverson's characters could be created
# by overstriking two characters on the type element.
# 
# The team then worked with IBM's Educational Marketing group to produce
# textbooks using the APL\360 version of Iverson's notation, and found some
# nearby teachers who agreed to use it for teaching their students
# mathematics. The result was an uproar.
#
# Mathematics teachers protested that APL was not mathematics and would confuse
# rather than enlighten students.  They also dislikee Iverson's use of
# mathematical terms such as rank to describe elements of his language.
# They also dislike the design decision to eliminate operator precedence.
# 
# Computer scientists disliked APL because it was not a standard
# procedural language like Cobol or Fortran.  It could not be punched
# on cards by 026 keypunches because its character set was not
# the IBM standard character set.  
#
# However, APL became very popular at IBM Research.  It eventually
# spread through IBM to become the language people used to create
# their own network applications rather than providing a work order
# the computing department.
#
# The APL community was very enthusiastic - almost messianic -- about
# their language.  The parts I worked on primarily were the APL soperating
# system (called APLSUP) and the model for accessing other systems from
# APL (Shared Variables).  I was elected chairman of the ANSI Standards
# group and editor of the ISO APL Standard that produced a 300 page
# document that was a modest but formal model of the rather
# rigorous semantics of APL that had been folded like origami into the
# seventy kilobyte interpreter.

# APL's downfall was the PC which was cheaper than timesharing because
# it could be purchased rather than paid for with a monthly bill.
#
#  
# The language that most closely resembles APL's semantics (but not
# its elegant notation) is probably no surprise to you; it's Python 3.
#
# The bridge between APL and compnet is the notion I have tried to
# advance with you that a computer network is primarly designed to
# be part of a large,
# interconnected computer, collection of computers that not a network.
# The Internet per se is roughly equivalent to the system bus in a
# computer architecture -- it simply provides an addressing scheme
# through which bits can be requested and sent back to a processing
# unit.  Its utility, like that of a computer, is that it is agnostic
# to what the bits are.  Application programmers can use its general
# model for delivering data to replace earlier, mostly analog,
# systems built and maintained specifically for a single
# application in the past.  Such systems include mail, telegraph,
# telephone, broadcast radio and television and catalog shopping.
#
# Since it is a computer, it needs a computer architecture.
#
# It is my hope that some of you will become very excited by the
# possibility of coming up with a much smaller and simpler formal
# description of the architecture of this new computer, one that
# does not have the many drawbacks of the one we are currently
# stuck with.  

# It will be pretty difficult to do this because this is not an
# undertaking that has textbooks and worked examples.
# My experience with Olin is that students have almost
# unlimited willingness to try new things that might have an impact
# on the world.

#
# The Proposal
#
# Starting Point: https://docs.python.org/3.3/howto/functional.html
#
# This is Python's "How to" for functional programming.  The essence
# of the idea is this: procedural languages like Fortran and Cobol
# dealt with data structures, but generally only treat hardware
# operations (which can complain and stop a program if, for example,
# a program attempts to divide by zero) as things that can stop a
# program.
#
# Object-oriented languages such as Java are supposed to treat
# user-defined data structures as first class object. One
# practical effect of this is that user-defined data structures
# can protect the internal consistency of their values by
# checking operations before they are performed.
#
# Functional programming languages treat functions themselves
# as objects.  Functions (or methods for object-oriented structures)
# can be put into data structures and bound to arguments under program
# control.
#
# It is this last property that is used in the (somewhat under construction)
# BJ_ module.
#
# When we look at a typical use of functional programming --
# a comprehension -- it is clear that as functional programs
# get larger, they tend not to fit on a line of a program
# and they tend to be unreadable.
#
# THe notion of the BJ_Stack is that if we break our programs
# down into well-defined layers  -- a thing that has been done in
# network programming since the 1960's -- it is possible to
# read them down the page rather than in a statement.
#
# The further concept of having each row of the stack be a part of
# a transform in which you map some request from its user form
# to its network form by a list of steps, each of which is invertible,
# lets us focus on one layer of the problem at a time and
# forces us to think about what is really required to make a layer
# atomic in the sense of being wholly independent of other layers
# in being able to map back to its original value.
#
# The goal is to allow the sublayers we are looking at in the BJ_
# module to describe each part of the network stack in a way that
# is easy to scan for its meaning, and easy to study a step at a time.
#
# By being able to compose independent layers into compound
# layers that are themselves invertible, we can create a stack
# in which the entire path from application client to application server
# is represented as a bijection, as is each small step.
#
# Finally, the goal of this model is to discover new primitive
# operations that could be realized in a computer built to run on
# a network.  The formalism of the BJ stack permits a type of
# checking for correctness that is similar to that provided for
# data objects in object-oriented programming.

# 
# The basic idea is that networks are layered for many reasons
# but when executing, each layer is called in turn to provide
# network services such as sending a packet from one computer to
# another.  The only important thing about a given source's use
# of a network layer is that there be a matching layer at the
# destination.   From a programming standpoint, what is important
# is that any message transformations (such as, in Morse code, from
# a series of words to a timed series of light blinks)  must have
# an inverse transform (from blinks back to words). We represent this
# in our protocol modeling mechanism by building small programs which are
# bijections - each small program has an inverse and the small program
# and the inverse are packaged and interpreted in a module consisting of
# several Python 3.3 classes.
#
# For example, a simple network function is encryption:
#  in an unencrypted system a universal datagram is sent
#  through the network from some host to another
#
# In a symmetric key system, the data is first encrypted
# with a key known to both parties, then decrypted with that key.
#
# The programs that do the encrytion are, in some case, the
# same.  For example, the  RC4 cypher works by using a key to
# create a random bit string, then xor'ing the input with
# that random bit string.  Thus, in RC4 at least, the
# inverse program is the same as the calling program.

# By forcing ourselves to use this functional programming model
# as we develop our description of a simple network we hope to
# produce a functional programming model that is both
# more accessible and easier to analylze and because of this 
# we are likely to come up with a more elegant way to
# think about the problems of the network.

# At least, that is the thesis of this class.

# Alex Morrow - February 5, 2014

# All classes begin with 'BJ' for bijection.
##########################################################################
# This is the basic set of bijection classes which we will start with
# in the class.  These will get more sophisticated as we go along.
#
# class BJ_Layer:
#     """basic bijection """
#     def __init__(self,name,fn,fn_inv):
#         """store function, function inverse and name of layer"""
#         self.name = name # the name of the "bijection" or transform
#         self._fn = fn  # the function
#         self._fn_inv = fn_inv # the function inverse
#
# class BJ_Dict(BJ_Layer):
#   "bijection based on invertible dictionary"
#     def __init__(self,name,Dict):
#         """create function and inverse from Dict"""
#        pass
#
# class BJ_SplitJoin(BJ_Layer):
#     """str bijection that uses Split to create substrings based on a separator,
#        character (str), then uses join to insert a new separation character."     
#     def __init__(self,name,Gen,Gen_inv):
#         """ stores a generator and its inverse generator"""
#
#
##########################################################################
#
# class BJ_Stack:
#     def __init__(self,tuple):
#     """ creates a bj_stack instance by stacking bj_layers from top to bottom"""
#         pass
#     def __call__(self,inDo):
#     """ calls stack from top with argument inDo #(i.e., in domain of fn)
#         pass
#     def inv(self,inCo):
#     """ calls stack from bottom with argument inCo #(i.e., in codomain of fn)
#     
#
# A single function and its inverse are called a BJ_Layer
# There are several types of BJ_Layer.  Perhaps the simplest
# bijection is a dictionary D having the property that
# len(D.keys())==len(D.values()). This was at one time
# called a 1-1 or invertable function, but is now referred to
# as a bijection.
#
# The class BJ_Dict(BJ_Layer). has a constructor that requires just
# a name and dictionary.   BJ_Dict("name,dictionary) poducs
# 
# 
# 
#
# The primary reason for using Python 3.3 is to be able to build these
# 
#

#
# In this unit, we look at the idea of these matching layers in a
# miniature context: sublayers of a Morse code implementation of
# a physical layer.
#


#
###########  some utility functions for debugging

#



DEBUG = True
TRACING = True

def nop(X,*T,**D):
    """ do nothing but return a value passed by the caller"""
    return X

def p(X,*T,**D):
    """print a value as a side effect, then return the value"""
    print(X,*T,**D)
    return X
##for the debug and trace functions:
##    these are intended to be used with the assert statement.
##    Python has a compiler flag -o that will remove assert statements
##    from your code while compiling i.
##
##    Thus, by using assert as the basis for the trace and debug functions,
##    you can insert debugging and trace functions ad lib, knowing they
##    will not take execution time if the -o flag is used.
def debug(X,*T,**D):
   
    if DEBUG:
        p(X,*T,**D) #prints the value and returns T
    return True # for assert statement

def trace(X,*T,**D):
    if TRACING:
        p(X,*T,**D)
    return True # for assert statement
#
# End of utility functions
#

#
## 
#


#
## BJ_Layer Base Class
#


class BJ_Layer:
    "Base class for other Layers"
    def __init__(self,
                 name = None,       # each transform should have a name
                 fn = None,
                 fn_inv = None  # from domain to codomain
                 ):
        """BJ_Layer(name,fn,fn_inv) """
  
        self.name = name
        self._fn = fn
        self._fn_inv = fn_inv

    def register_stack(self,stack_self):
        "Give the layer a way to contact the stack"
        self._stack = stack_self
        return
        
    def __call__(self,in_Do):
        return self._fn(in_Do)

    def inv(self,in_Co):
        return self._fn_inv(in_Co)
            
class BJ_Iter(BJ_Layer):
    "Iterable"
   
    def __call__(self,inDo):
        if type(inDo) in (list,tuple):
            return [self._fn(d) for d in inDo]

        return self._fn(inDo)
        
    def inv(self,inCo):
        if type(inCo) in (list,tuple):
            return [self._fn_inv(c) for c in inCo]

        return self._fn_inv(inCo)

#
## BJ_Dict
#

class BJ_DictSep(BJ_Dict):
    "this implements many-to-one character map using sep character to find substrings"

    def __init__(self,name,Dict=None,find_sep='',replace_sep=''):
        self._find_sep = find_sep
        self._replace_sep = replace_sep
        super().__init__(name=name,Dict=Dict)

        
    
    def __call__(self,inDo):
        """Note a given replace_sep is specific to a single BJ_Layer -- it is the key to
        the replace_sep --> find_sep reverse transform for a given BJ_layer
        in the stack and can therefore
        only be used once in a stack"""
        
        if not is_str(inDo):
            raise DomainError("argument not a str")
        if self._replace_sep in self._replace_sep_list:
            raise SepError("replace_sep string '{}' already in use in this stack".format(self.stack.replace_sep_list))
#--------------------------------------------------------------------------------------------
        Z = self._replace_sep.join([x for x in inDo.split(self._find_sep) if not self.replace_sep in self.stack._replace_sep_list])
#--------------------------------------------------------------------------------------------
        self.stack.replace_sep_list.append(self._replace_sep)
         
    
    def inv(self,inCo):
        
        if not is_str(inCo):
            raise DomainError("argument not a str")
#--------------------------------------------------------------------------------------------
        return self._find_sep.join([x for x in inCo.split(self._replace_sep)])
#--------------------------------------------------------------------------------------------
    
        
        
        
        
            



class BJ_Iter(BJ_Layer):
    
    def __call__(self,inDo):
        
        if is_iterator(inDo):
            return [self._fn(x) for x in inDo]

        if is_iterable(inDo):
            return "".join([self._fn(x) for x in inDo])

        return self._fn(inDo)
        

    def inv(self,inCo):
        if is_iterator(inCo):
            return [self._fn_inv(x) for x in inCo]

        if is_iterable(inCo):
            return "".join([self._fn(x) for x in inCo])
        return self._fn_inv(inCo)


class BJ_Dict(BJ_Iter):
    "Dictionary-based layer"
    def __init__(self,name,Dict=None):
        "BJ_Dict(name,Dict)"
        if Dict is None:
            assert warning("No Dictionary Provided.  This Layer is a pass-through (no-op)")
            super().__init__(name=name,
                             fn=lambda x:x,
                             fn_inv=lambda x:x)
        else:
            
            if len(set(Dict.values())) != len(Dict):
                raise TypeError("Dict not invertible")
            self._dict = Dict
        
        
    
        self._dict_inv = {v:k for (k,v) in Dict.items()}
        
        super().__init__(name=name,
            fn = lambda inDo:self._dict[inDo],
            fn_inv = lambda inCo: self._dict_inv[p(inCo)]
            )

#
# BJ_Stack - controls the use of BJ_Layers
#
class BJ_Stack:
    def __init__(self,BJLayers):
        
        "Initialize stack layers"
        self._stack = tuple(BJLayers)
        for layer in self._stack:
            layer.register(self)
            
    def __len__(self):
        return len(self._stack)

    def __repr__(self): # display names of stack levels and \
                        # number them from [0] to [n]
        
        return (
            "\n".join(
                ["Level     Name"]+
                ["[{:2}]\t{}".format(number,name) for number,name in enumerate(
                    [layer.name for layer in self._stack])]))

    def descend(self,in_Do):
        "Start stack recursion"
        return self.descend_step(self._stack,in_Do) 
        
    def descend_step(self,stack,in_Do):
        "descending a step on stack"

        Z = p(stack[0](p(in_Do)))

        assert trace("In descend_step on stack. {}({}) --> {}".format(stack[0].name,in_Do,Z))

        if len(stack)<2:
            return Z
        
        if type(Z) is list:
            return [self.descend_step(stack[1:],z) for z in Z]
       
        return self.descend_step(stack[1:],Z) 

    def climb(self,in_Co):
        "climbing stack"
        
        return self.climb_step(self._stack,in_Co)

    def climb_step(self,stack,in_Co):
        "climbing stack"

        #print(len(stack),"\n",repr(stack),"\n")

        Z = stack[-1].inv(in_Co)

        assert trace("climbing: {}.inv({}) --> {}".format(stack[0].name,in_Co,Z))

        if len(stack) < 2:
            return Z
        if type(Z) is list:
            return [self.climb_step(stack[:-1],z) for z in Z]
        return self.climb_step(stack[:-1],Z) 
    
    def dual(self,fn,in_Do):
        return self.climb(fn(self.descend(in_Do)))


            
if __name__ == "__main__":
    
    fwi = BJ_Dict(name="[1 to 'Ghost of 1']",
                  Dict={1:"Ghost of 1"}
                  )
    fwi2 = BJ_Dict(name="['ghost of 1' to 'compnet student']",
                   Dict={"Ghost of 1":"compnet student"})


    stack=BJ_Stack([fwi,fwi2])
    
    p(stack)

    p(stack.dual(p,1))






    

    
    

    



    
        


    

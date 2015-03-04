#
## Basic BiJection
#
DEBUG = False

def p(X,*T,**D):
    print(X,*T,**D)
    return X

def debug(X,*T,**D):
    if DEBUG:
        p(X,*T,**D)
    return True

class BJ_Stack:
    def __init__(self,BJs):
        stack = []
        for BJ in BJs:
            stack += [BJ]
        self._stack = tuple(stack)
        
    def __len__(self):
        return len(stack)

    def __repr__(self):
        return "\n".join("{}".format(BJ.__doc__ for BJ in self._stack))

    def climb(self,in_Co):
        return self.climb_steps(self._stack,in_Co)

    def climb_steps(self,stack,in_Co):
        if len(stack) == 0:
            return in_Co
        return self.climb_steps(stack[:-1],stack[-1].inv(in_Co))

    def descend(self,in_Do):
        return self.descend_steps(self._stack,in_Do)
        
    def descend_steps(self,stack,in_Do):
        if len(stack) == 0:
            return in_Do
        return self.descend_steps(stack[1:],stack[0](in_Do))
    
    def dual(self,fn,in_Do):
        return self.climb(fn(self.descend(in_Do)))
#
## BJ_Layer
#


class BJ_Layer:
    def __init__(self,
                 fn=  lambda inDo:inDo,
                 fn_inv= None):
        self._fn = fn
        if fn_inv is None:
            self._fn_inv = fn.inv
        else:
            self._fn_inv = fn_inv
        
    def __call__(self,inDo,*T,**D):
        """descending call """
        
        assert debug(self.__call__.__doc__)
        assert debug("__call__({},{},{})".format(inDo,T,D))
        
        """ descending call fn(X) """
        return self._fn(inDo,*T,**D)

    def inv(self,inCo,*T,**D):
        """climbing call"""
        
        assert debug(self.inv.__doc__)
        assert debug("inv({},{},{})".format(inCo,T,D))
        
        return debug(self._fn_inv(inCo,*T,**D))


#
## BJ_Dict
#

class BJ_Dict(BJ_Layer):
    def __init__(self,Dict):
        self._dict = Dict
        self._dict_inv = {v:k for (k,v) in Dict.items()}
        super().__init__(
            fn = lambda inDo:self._dict[inDo],
            fn_inv = lambda inCo: self._dict_inv[inCo]
            )


if __name__ == "__main__":
    
    fwi = BJ_Dict({1:2,2:1})
    fwi2 = BJ_Dict({2:3,3:2})
    p(fwi)
    p(fwi2)
    p (1 == fwi.inv(fwi(1)))
    p("")
    p(BJ_Stack([fwi,fwi]).dual(p,1))
    p("")
    p(BJ_Stack([fwi,fwi2]).dual(p,1))





    

    
    

    



    
        


    

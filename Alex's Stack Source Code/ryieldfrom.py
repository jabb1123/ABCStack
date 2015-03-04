#
## recursive " yield from "
#



def ryf(X):
    if not hasattr(X,"__len__"):
        yield X
    else:
        for x in X:
            yield from ryf(x)
            
def flatten(X):
    return [i for i in ryf(X)]


if __name__ == "__main__":
    
    test =[1, [2, [3, 4, [5, [6], 7], 8, 9, 10], (11, (12, (13, 14), 15), 16), 17], 18, [[[19, 20]]]]
    

    print(flatten(test))

    

    

        
        

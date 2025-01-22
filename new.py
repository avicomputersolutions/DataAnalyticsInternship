def Recursive(low,high):
    if low == high:
        return 
    print(low)
    Recursive(low+1,high)

def RecursiveTD(high,low):
    if high == low:
        return 
    print(high)
    RecursiveTD(high-1,low)

def fact(n):
    if n==0:
        return 1
    else :
        return n * fact(n-1)
    
def someFunction(*arg):
    print(arg)

def newFunction(**kwarg):
    print(kwarg)

if __name__ =="__main__":
    newFunction(name="Garvita",hometown="indore",habit="Foody")
    fact(5)
    RecursiveTD(10,0)
    Recursive(0,10)
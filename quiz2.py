# def threesquares(n) :
#     for i in range(0,n):
#         while n>0 and i :
#             if(n = )


def repfree(s):
    return len(set(s)) == len(s)
        
print(repfree("zb%78"))


def ascending(l) :
    if len(l) <= 1:
        return True
    else :
        return(l[0] < l[1] and ascending(l[1:]))
    
print(ascending([1,2,3,6,5]))

def descending(l) :
    if len(l) <= 1:
        return True
    else :
        return(l[0] > l[1] and descending(l[1:]))

print(descending([6,5,4,3]))
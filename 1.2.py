# Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise.
# However, your function cannot use the multiplication, modulo, or division operators


def even(k):
    return k&1==0 #binary operator '&' is used ☆*: .｡. o(≧▽≦)o .｡.:*☆
print (even(14))

#OR:
def even(k):
    if k&1==0:
        return True
    else: 
        return False
    
print (even(14))

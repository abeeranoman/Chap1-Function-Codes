#Write a short Python function, is multiple(n, m),
#  that takes two integer values and returns True if 
# n is a multiple of m, that is ,n = mi for some integer i,and
# False otherwise.


def is_multiple(n, m):
    if m==0:
        return False
    if n%m == 0:
        return True
    else:
        return False
    
n = int(input("Enter your first num"))
m = int(input("Enter your second num"))
print (is_multiple(n, m))


'''OR'''

def is_multiple(n, m):
    return m!= 0 and n%m == 0 #return automatically returns True or False ☆*: .｡. o(≧▽≦)o .｡.:*☆
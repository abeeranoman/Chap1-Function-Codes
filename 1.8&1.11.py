#1.8: Python allows negative integers to be used as indices into a sequence, such as a string.
#  If string s has length n, and expression s[k] is used for in dex −n≤ k <0,what is the equivalent index j≥0 such that s[j] references the same element?
# in other words convert negative index into a positive one
# The relationship between k and j is: j = n + k -- since j is positive while k is negative but can be corrected by adding n.
def convertindex(k,n):
    return n + k

#s = "HELLO"
#n = len(s)   # length = 5

print (convertindex(-1,5)) #4

print (convertindex(-3,5)) #2

print (convertindex(-5,5)) #0


#1.11: Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
def listmaker(n):
    result = [2**i for i in range(n)] 
    return result
print (listmaker(9))
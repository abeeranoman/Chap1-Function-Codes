# Demonstrate how to use Python’s list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
def getlist(n):
    numbers =[i* (i+1) for i in range(10)]
    return numbers
print( getlist(10))
       
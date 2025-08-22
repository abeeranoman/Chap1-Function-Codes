#1.6: Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.
def sumOfOddSquares(n):
    total = 0 
    for i in range(1,n):
        if i % 2 > 0: 
            total += i*i
    return (total)

print (sumOfOddSquares(8))    

# 1.7: Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function.
print (sum(i*i for i in range (1,10) if i % 2 > 0))
#Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.

def odd(n):
    total = 0
    for i in range(n):
        if i%2 != 0:    #for odd
            if i > 0:   #for positive ☆*: .｡. o(≧▽≦)o .｡.:*☆
                total += i * i  
    return total

n = 10
print(odd(n))

#OR: (simpler using range)

def odd(n):
    total = 0
    for i in range(1, n, 2):
        total += i*i 
    return total
n = 14
print(odd(n))

# Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function.

print(sum(i * i for i in range(int(input("Enter your number n: ")))))
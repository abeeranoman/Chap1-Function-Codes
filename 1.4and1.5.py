# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def squares(n):
    total = 0
    for i in range(n):
        total+= i*i
    return total

n = 4
print(squares(20))

#Give a single command that computes the sum from Exercise R-1.4, relying on Python’s comprehension syntax and the built-in sum function.

print (sum(i * i for i in range(int(input("Enter the number n: ")))))


#Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.

class OddSumCal:
    def __init__(self, n: int):
        self.n = n

    def Odd(self):
        total = 0
        for i in range(self.n):
            if i != 0:
                if i > 0:
                    total += i**2
        return total
    
    def __str__(self):
        return f"The sum of all odd squares less than {self.n} is: {self.Odd()}"
    
n = int(input("Enter your number."))
if not isinstance(n, int):
    raise ValueError
List = OddSumCal(n)
print(List.Odd())
'''
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
'''
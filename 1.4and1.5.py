# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.
class Squares:
    def __init__(self, n: int):
        self.n = n
    def squares(self):
        total = 0
        for i in range(self.n):
            total+= i*i
        return total

    def __str__(self):
        return f"The sum of all positive integers: {self.squares()}"
    
n = 9
List = Squares(n)
result = List.squares()
print(List)

    #Give a single command that computes the sum from Exercise R-1.4, relying on Python’s comprehension syntax and the built-in sum function.

    #print (sum(i * i for i in range(int(input("Enter the number n: ")))))


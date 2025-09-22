# Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of 
# length two. Do not use the built-in functions min or max in implementing your solution.

class Minmax:
    def __init__(self, data):
        self.data = data 

    def minmax(self):
        smallest = largest = self.data[0] #assume that the first num in the data is the smallest/largest ☆*: .｡. o(≧▽≦)o .｡.:*☆
    
        for num in self.data:
            if num < smallest:
                smallest = num 
        
            if num > largest:
                largest = num 

        return smallest, largest
    
    def __str__(self):
        smallest, largest = self.minmax()
        return f"Smallest: {smallest}, Largest: {largest}"
    
    

data = [1, 6 , 4, 100, 73, 0.3]
Num = Minmax(data)
result = Num.minmax()
print(Num)
#print(Num)


    
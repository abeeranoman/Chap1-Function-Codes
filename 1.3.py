# Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of 
# length two. Do not use the built-in functions min or max in implementing your solution.


def minmax(data):
    smallest = largest = data[0] #assume that the first num in the data is the smallest/largest ☆*: .｡. o(≧▽≦)o .｡.:*☆
    
    for num in data:
        if num < smallest:
            smallest = num 
        
        if num > largest:
            largest = num 

    return smallest, largest

nums = [1, 6 , 4, 100, 73, 0.3]
print (minmax(nums))

    
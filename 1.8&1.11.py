#1.8: Python allows negative integers to be used as indices into a sequence, such as a string.
#  If string s has length n, and expression s[k] is used for in dex −n≤ k <0,what is the equivalent index j≥0 such that s[j] references the same element?
# in other words convert negative index into a positive one.


# The relationship between k and j is: j = n + k -- since j is positive while k is negative but can be corrected by adding n.
class IndicesConverter:
    def __init__(self, k, s):
        self.k = k
        self.s =s 

    def converter(self):
        n = len(self.s)
        if -n < self.k <= 0:
            j = n + self.k
            return j

        elif  0 <= self.k < n:
            return self.k
        
        else: 
            return None
        
    def __str__(self):
        p = self.converter()
        if p is None:
            return f"Index {self.k} is out of range for '{self.s}'"
        else:
            return f"Index {self.k} corresponds to {p}, character = '{self.s[p]}'"

        
        

s = input("Enter your string: ")
n = int(input("Enter an  index: "))
Text = IndicesConverter(n, s)
result = Text.converter()
print(Text)

    

   
    

        

#This code allows diversity (so all the load will be on the main block)

#1.11: Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
#def listmaker(n):
 #   result = [2**i for i in range(n)] 
 #   return result
#print (listmaker(9))
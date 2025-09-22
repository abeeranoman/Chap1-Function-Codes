# Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise.
# However, your function cannot use the multiplication, modulo, or division operators

class EvenOrOdd:
    def __init__(self, k):
        self.k = k


    def even(self):
        return (self.k & 1) ==0 #binary operator '&' is used ☆*: .｡. o(≧▽≦)o .｡.:*☆
   

    def __str__(self):
        return f"{self.k} → {self.even()}"
        
k = int(input("Enter a number"))
Num = EvenOrOdd(k)
result = Num.even()

if result:
    print("The number is even")
else:
    print("The number is odd")
        
'''OR:
def even(k):
    if k&1==0:
        return True
    else: 
        return False
    
print (even(14))
'''
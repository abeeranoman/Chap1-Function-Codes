#Write a short Python function, is multiple(n, m),
#  that takes two integer values and returns True if 
# n is a multiple of m, that is ,n = mi for some integer i,and
# False otherwise.

class MultCal:
    def __init__ (self, n, m):
        self.n = n 
        self.m = m

    def is_multiple(self):
        if self.m==0:
            return False
        if self.n % self.m == 0:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.m} and {self.n} → Multiple: {is_multiple}"
    
n = int(input("Enter your first num"))
m = int(input("Enter your second num"))
calc = MultCal(n, m)
result = calc.is_multiple()
if result:
    print(f"{n} is a multiple of {m}")
else:
    print(f"{n} is NOT a multiple of {m}")

#'''OR'''

#def is_multiple(n, m):
    #return m!= 0 and n%m == 0 #return automatically returns True or False ☆*: .｡. o(≧▽≦)o .｡.:*☆
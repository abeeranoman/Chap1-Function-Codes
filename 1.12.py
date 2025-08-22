# Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version of the choice function
import random
def getnumber(data):
    index = random.randrange(len(data)) #(len(data)) for a random length number that further identifies an index
    return data[index]
print (getnumber((2,5,4,7,9,0)))
#randrange gives 1 random out of the liat whereas range gives us a list till n-1.
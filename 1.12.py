# Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version of the choice function
import random
def getnumber(data):
    index = random.randrange(len(data))
    result = data[index]
    return result

num = (9, 7, 3, 3, 5, 4)
print (getnumber(num))

'''Key difference between range and randrange is that randrange gives us 1 random (they both follow the m till n-1 rule)'''
# Demonstrate how to use Python’s list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

def List():
    empty = []
    i = 0
    for i in range (0, 10 , 1):
        total = i * (i + 1) 
        empty.append(total)
    return empty

print (List())


#---------OR-----------

one_List = [i * (i + 1) for i in range(0, 10, 1)]
print(one_List)


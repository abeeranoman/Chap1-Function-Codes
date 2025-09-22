class NumberList:
    def __init__(self, data):
        self.data = data

class MinMaxCalculator:
    def __init__(self, num_list: NumberList):
        self.num_list = num_list

    def minmax(self):
        if not self.num_list.data: #if their is no data in NumberList
            return (None, None) #(largest, smallest)
        
        smallest = largest = self.num_list.data[0]
        for i in self.num_list.data:

            if smallest > i:
                smallest = i

            if largest < i:
                largest = i 
            
        return (smallest, largest)
    
    def __str__(self):
        largest, smallest = self.minmax()
        if smallest is None or largest is None:
            return  f"The list  is empty"
        
        return f"The smallest number in the list: {smallest}.\n The largest number in the list: {largest}"
    
List = NumberList([9, 7, 5, 3, 2, 0.1])
v1 = MinMaxCalculator(List)
result = v1.minmax()
print (v1)
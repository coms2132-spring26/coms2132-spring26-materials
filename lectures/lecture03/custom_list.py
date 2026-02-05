class MyList(list):
    
    def reversed(self):
        """
        Return a new list with the elements in reversed order
        """
        return self[::-1]
    
class MyCompositionList():
    
    def __init__(self):
        self.the_list = []

    def append(self, element):
        self.the_list.append(element)

    def reversed(self):
        """
        Return a new list with the elements in reversed order
        """
        return self.the_list[::-1]   

li = MyCompositionList()
li.append(1)
li.append(2)
li.append(3)
print(li.reversed())
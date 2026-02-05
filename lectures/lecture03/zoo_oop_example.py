
#simba = ("Lion", 5, "yellow") # tuple 
#nala = ("Lion", 4, "white") 
#
#animal_list = [simba, nala]
#
#simba_name = "Lion"
#simba_age = 5
#simba_fur_color = "yellow"

#a = [1,2,3]
#print(a.__len__())
#print(len(a))

class Animal:
    
    def __init__(self):
        self.name = "unknown"
        self.stomach = []

    def eat(self, food):
        self.stomach.append(food)

    def speak(self,): 
        print(f"My name is {self.name}")

class Lion(Animal): 

    def __init__(self, name, age, color ): # Constructor
        super().__init__() # call the parent constructor 
        self.name = name
        self.age = age
        self.fur_color = color

    def speak(self):
        print(f"ROAR, my name is {self.name}")

class Elephant(Animal):

    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age 

    

nala = Lion("Nala", 4, "white")
simba = Lion("Simba", 5, "yellow")
dumbo = Elephant("Dumbo", 6)

#simba.eat("chicken")
#elephant.eat("leaves")

#animals = [nala, simba, elephant]
#for animal in animals: 
#    animal.speak()

#print(isinstance(nala, Animal))
nala.eat("chicken")
print(nala.stomach)

dumbo.speak()
nala.speak()
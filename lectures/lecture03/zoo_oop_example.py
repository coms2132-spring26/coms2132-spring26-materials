
#simba = ("Lion", 5, "yellow") # tuple 
#nala = ("Lion", 4, "white") 
#
#animal_list = [simba, nala]
#
#simba_name = "Lion"
#simba_age = 5
#simba_fur_color = "yellow"

a = [1,2,3]
print(a.__len__())
print(len(a))

class Lion: 

    def __init__(self, name, age, color ): # Constructor
        self.name = name
        self.age = age
        self.fur_color = color

    def speak(self):
        print(f"ROAR, my name is {self.name}")

class Elephant:

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def speak(self,): 
        print(f"Tooot: My name is {self.name}")

nala = Lion("Nala", 4, "white")
simba = Lion("Simba", 5, "yellow")
elephant = Elephant("Dumbo", 6)

animals = [nala, simba, elephant]
for animal in animals: 
    animal.speak()

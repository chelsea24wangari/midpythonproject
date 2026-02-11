class Animal:
    isMammal = True

    def speak(self):
        print("Animal is speaking")

    def move(self):
        print("Animal is moving")

class Cat:
    def sound(self):
        print("Cat is meowing")

    def climb(self):
        print("Cat is climbing a tree")

class Horse(Animal):
    hasTail = True

    def neigh(self):
        print("Horse is neighing")

a  = Animal()



c  = Cat()
h  = Horse()

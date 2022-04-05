class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 40
        self.energy = 20
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.health += 10
        self.energy += 5
        return self

    def play (self):
        self.health += 5
        return self

    def noise(self):
        print (self.noise)

class Ninja (Pet):
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet


    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        return self
        
    def bathe(self):
        self.pet.noise
        return self

bluehorse = Pet("Bluehorse", "horse", "shake hands", "neigh")
john = Ninja("John", "Doe", "oats", "hay", bluehorse)

john.feed().walk().bathe()
'''
*************************
EJERCICIO POU JOSÉ ABREU
*************************
'''
import random

class Pou:
  # iniciar
  def __init__(self, name):
    self.name = name
    self.age = 0
    self.hunger = 0
    self.energy = 0
    self.happiness = 0
    self.health = 0
    self.alive = True

  def status(self):
    print("Name:", self.name)
    print("Age:", self.age)
    print("Hunger:", self.hunger)
    print("Energy:", self.energy)
    print("Happiness:", self.happiness)
    print("Health:", self.health)

  def __str__(self):
    return f"Name: {self.name}\nAge: {self.age}\nHunger: {self.hunger}\nEnergy: {self.energy}\nHappiness: {self.happiness}\nHealth: {self.health}"


def play(self):
    self.hunger += random.randint(1, 3)
    self.energy -= random.randint(1, 2)
    self.happiness += random.randint(2, 4)
    self.health -= random.randint(1, 2)
    self.age += 1

def eat(self):
    self.hunger -= random.randint(2, 4)
    self.energy += random.randint(1, 3)
    self.health += random.randint(1, 2)

def sleep(self):
    self.energy += random.randint(2, 4)
    self.health += random.randint(1, 3)

toto = Pou("Toto")

while True:
    toto.status()  # Display Pou's status before every action
    option = input("What do you want to do? (play, eat, sleep, exit): ")

    if option == "play":
        toto.play()
    elif option == "eat":
        toto.eat()
    elif option == "sleep":
        toto.sleep()
    elif option == "exit":
        break
    else:
        print("Invalid option. Try again.")


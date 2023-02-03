import random
import copy


class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color


harry = Animal('hippogriff', 6, 'pink')
harriet = copy.copy(harry)

print(harry.species)
print(harriet.species)

''' 
  work with lists
'''

harry = Animal('hippogriff', 6, 'pink')
carrie = Animal('chimera', 4, 'green polka dots')
billy = Animal('bogill', 0, 'paisley')
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)

print(more_animals[0].species)
print(more_animals[1].species)
my_animals[0].species = 'ghoul'
print(my_animals[0].species)

'''
  random number
'''
print(random.randint(0, 100))
num = random.randint(1, 100)
# while True:
#     print('Guess a number between 1 and 100')
#     guess = int(input())
#     if guess == num:
#         print('you guessed right')
#         break
#     elif guess < num:
#         print('Try higher')
#     elif guess > num:
#         print('Try lower')
'''
  pick random item from a list
'''
dessert = ['ice cream', 'pancakes', 'brownie', 'cookies', 'candy']
print(random.choice(dessert))
# print(dessert[random.randint(0, len(dessert)-1)])

'''
  shuffle list
'''
random.shuffle(dessert)
print(dessert)

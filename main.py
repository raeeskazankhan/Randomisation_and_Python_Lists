import random

# random_integer = random.randint(1, 10)
# print(random_integer)
#
# random_float = random.random() * 5
# print(random_float)

# HEADs OR TAILS

# random_dice = random.randint(0, 1)
#
# if random_dice == 0:
#     print("Tails")
# else:
#     print("Heads")

# BANKER ROULETTE
names_string = input("Give everybody's name, separated by a comma: ")
names = names_string.split(", ")

random_person = random.randint(0, len(names) - 1)
person_to_pay = names[random_person]

print(f"{person_to_pay} is going to pay for the meal today!")

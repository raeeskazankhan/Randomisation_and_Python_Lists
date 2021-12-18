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
# names_string = input("Give everybody's name,  separated by a comma: ")
# names = names_string.split(", ")
#
# random_person = random.randint(0, len(names) - 1)
# person_to_pay = names[random_person]
#
# print(f"{person_to_pay} is going to pay for the meal today!")

# TREASURE MAP
# row1 = ["O", "O", "O"]
# row2 = ["O", "O", "O"]
# row3 = ["O", "O", "O"]
# maps = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}\n")
# position = input("Where do you want to put the treasure: ")
#
# row_value = int(position[0]) - 1
# column_value = int(position[1]) - 1
# maps[column_value][row_value] = "X"
#
# print(f"{row1}\n{row2}\n{row3}\n")

# ROCK PAPER SCISSORS
hand_signals = ["ROCK", "PAPER", "SCISSORS"]
random_hand_signal = random.randint(0, 2)
computer_answer = hand_signals[random_hand_signal]
print(computer_answer)
user_answer = input("Enter your Choice: ROCK, PAPER or SCISSORS: ")

final_verdict = ""
if computer_answer == "ROCK" and user_answer == "SCISSORS":
    final_verdict = "COMPUTER WINS, YOU LOOSE"
elif computer_answer == "SCISSORS" and user_answer == "PAPER":
    final_verdict = "COMPUTER WINS, YOU LOOSE"
elif computer_answer == "PAPER" and user_answer == "ROCK":
    final_verdict = "COMPUTER WINS, YOU LOOSE"
elif computer_answer == user_answer:
    final_verdict = "DRAW"
else:
    final_verdict = "YOU WON!"

print(f"YOU HAVE CHOSEN: {user_answer}")
print(f"COMPUTER HAS CHOSEN: {computer_answer}")
print(f"FINAL VERDICT: {final_verdict}")

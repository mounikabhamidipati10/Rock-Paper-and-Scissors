 # import random module
import random
# create function to get_computers_choice, variable to store random range, dict to store key and values, variable to store random number, return variable
def get_computers_choice():
    random_number = random.randint(1,3)

    options = {1:"rock", 2:"paper", 3:"scissors"}
    computers_choice = options[random_number]

    return computers_choice
# create function to get_user_input, variable to store user_input from use and convert into lowercase(), return variable
def get_user_input():
    user_input = input("Enter rock/paper/scissors: ")
    user_input = user_input.lower()

    return user_input
# create function get_result to compare 2 inputs and print result with parameters and if-elif statement
def get_result(user_input, computers_choice):
    if computers_choice == user_input:
        return "draw"
    elif user_input == "paper" and computers_choice == "rock":
        return "win"
    elif user_input == "rock" and computers_choice == "scissors":
        return "win"
    elif user_input == "scissors" and computers_choice == "paper":
        return "win"
    else:
        return "lose"

# outside the function create variable to call computers_choice
computers_choice = get_computers_choice()

# now write code to handle wrong  user inputs
while (True):
    user_input = get_user_input()
    if user_input in ["rock", "paper", "scissors"]:
        break
result = get_result(user_input, computers_choice)

# Now print the result
print("-" * 50)
print("\t\tComputer's choice: {}".format(computers_choice))
print("\t\tUser input: {}".format(user_input))
print("-" * 50)
print("\t\tFinal Result: {}".format(result))
print("=" * 50)

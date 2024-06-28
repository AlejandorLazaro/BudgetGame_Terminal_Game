import random

def budget_game():
    #set up variables
    bank_account = random.randint(0, 1000)
    expense = 0
    deposit = 0

    print(f"Hello! Welcome to budget game, you currently have ${bank_account} dollars in your account.")

    if bank_account >= expense:
        print("You have enough money to buy an item, what would you like to buy?")
    else:
        print("You have reached your budget! You can either work some more or return the item. Which would you like to do?")

budget_game()
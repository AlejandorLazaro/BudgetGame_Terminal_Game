import random

def budget_game():
    #set up variables
    bank_account = random.randint(0, 1000)
    expense_amount = 0
    savings_account = 0

    print(f"Hello! Welcome to budget game, you currently have ${bank_account} dollars in your account.")

    while bank_account > 0:
        expense_item = input("You have enough money to buy an item, what would you like to buy?")
        item_cost = int(input((f"How much does the {expense_item} cost?")))
        
        if item_cost < bank_account:
            expense_amount += item_cost
            bank_account -= expense_amount
            print(f"You bought {expense_item}, they cost ${item_cost} dollars.")
            print(f"You have ${bank_account} dollars left in your account.")
        else:
            print("You don't have enough money to buy this item.")
            print("Game over, thanks for playing!")

        #ask the user what to do next

        if bank_account > 0:

            action = input("Would you rather save your money or buy something else? (save/buy):").strip().lower()

        if action == "save":
             savings_account += bank_account
             bank_account = 0
             print(f"You decided to save your money. You have saved ${savings_account} dollars!")
             break
             
        elif action == "buy":
            continue
        else:
            print("Can't choose that, Please select either 'save' or 'buy'.")

        if bank_account == 0 and savings_account == 0:
            print('You have no money left to spend or save.')
        elif savings_account > 0:
            print(f"Game over. You have saved ${savings_account} dollars.")
budget_game()
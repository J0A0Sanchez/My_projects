
def shopping(list):
    type_list = []


    item_quantity = int(input("How many items did you buy while shopping today? "))
    for c in range(1, item_quantity + 1):
        item = input(f"Enter the {c}º item: ").strip().title()
        if item in list:
            list.remove(item)
        else:
            type_list.append(item)

    print(f"\nThis is your updated shopping list: {list}")
    print(f"You have {len(list)} items left on it.")
    print(f"These are the items you bought that were not on the list: {type_list}\n")

    while True:
        additional_items = input("Do you want to add items to your shopping list? Type 'y' for yes or 'n' for no: ").strip().lower()
        if additional_items == "n":
            break
        elif additional_items == "y":
            item_quantity = int(input("How many items do you want to add? "))
            for c in range(1, item_quantity + 1):
                item = input(f"Enter the {c}º item to add: ").strip().title()
                if item not in list:
                    list.append(item)
        else:
            print("Invalid input. Please type 'y' or 'n'.")

    print(f"\nYour final shopping list is: {list}")



shopping_list = [
    "Jeans",
    "Sneakers",
    "Socks",
    "Cap",
    "Sunglasses",
    "Backpack",
    "Perfume",
    "Watch",
    "Belt"
]

shopping(shopping_list)

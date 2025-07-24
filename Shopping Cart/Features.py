def inputCheck(userInputItem):
    return userInputItem.lower().strip()


def printCurrentCart(lst):
    print()
    print('Shopping list:')
    for key, val in lst.items():
        quantity = val['quantity']
        print(f'- {key.capitalize()} x{quantity}' if quantity > 1 else f'- {key.capitalize()}')


def addItem(item, qty, lst):
    if item not in lst:
        lst[item] = {'quantity': qty}
    else:
        currentQty = lst[item].get('quantity', 0)
        lst[item]['quantity'] += qty


def removeItem(item, lst):
    if item not in lst:
        print(f"{item.capitalize()} is not in your cart!")
        return

    while True:
        userInput = input(f'All units of {item.capitalize()} or just a part? (A for All │ P for partial): ').lower()
        if userInput not in ['a', 'p']:
            print("Invalid option. Enter 'A' or 'P'.")
            continue
        break

    if userInput == 'a':
        del lst[item]
        printCurrentCart(lst)
    else:
        try:
            userInputUnitsToRemove = int(input(f'How many units of {item.capitalize()} do you want to remove ?: '))
        except ValueError:
            print("That's not a valid number.")
            return

        if userInputUnitsToRemove <= 0:
            print("Quantity to remove must be greater than 0.")
            return

        currentQty = lst[item]['quantity']

        if userInputUnitsToRemove > currentQty:
            print('Error: you want to remove more units than you have.')
        elif userInputUnitsToRemove == currentQty:
            del lst[item]
            printCurrentCart(lst)
        else:
            lst[item]['quantity'] = currentQty - userInputUnitsToRemove
            printCurrentCart(lst)


def checkOutTotal(lst, inventory):
    total = 0

    for itemName, data in lst.items():
        quantity = data['quantity']
        itemPrice = inventory.get(itemName.capitalize())

        if itemPrice:
            total += quantity * itemPrice
        else:
            print(f"{itemName.capitalize()} not found in inventory!")

    return total
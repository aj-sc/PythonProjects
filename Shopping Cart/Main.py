from Features import (
    inputCheck,
    printCurrentCart,
    addItem,
    removeItem,
    checkOutTotal
)

def shoppingCart():
    shoppingCartList = {}

    inventory = {
        'Tomate': 500,
        'Cebolla': 600,
        'Ajo': 300,
        'Leche': 5000,
        'Atun': 7000,
        'Jamon': 8500,
        'Pepino': 1200
    }

    print('''- Write the items you want to register
- Press O to checkout
- Press X to exit
- Press R to remove an item
- Press C to clear the cart
''')

    while True:
        userInputItem = inputCheck(input('What product do you want to buy ?: '))

        if not userInputItem:
            print('Error, type a valid product')
            continue

        match userInputItem:
            case 'o':
                if shoppingCartList:
                    printCurrentCart(shoppingCartList)
                    total = checkOutTotal(shoppingCartList, inventory)
                    print(f'Your total is: ${total:.2f}')
                    print('Come back later!')
                else:
                    print('Your cart is empty. Bye!')
                break

            case 'c':
                shoppingCartList.clear()
                print('Your cart is now empty!')

            case 'x':
                print('No items saved, bye!')
                break

            case 'r':
                userInputItem = inputCheck(input('What product do you want to remove ?: '))
                removeItem(userInputItem, shoppingCartList)

            case _:
                if userInputItem.isalpha():
                    while True:
                        userInputItemQty = input('And the quantity ?: ')
                        if not userInputItemQty.isdigit():
                            print('Not a valid number.')
                            continue

                        userInputItemQty = int(userInputItemQty)

                        if userInputItemQty <= 0:
                            print('Quantity must be greater than 0.')
                            continue
                        break

                    addItem(userInputItem, userInputItemQty, shoppingCartList)
                    printCurrentCart(shoppingCartList)
                else:
                    print('Error, type a valid product name (letters only).')

shoppingCart()
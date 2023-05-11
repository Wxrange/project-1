def main_menu():
    print('----MAIN MENU----')
    print('s: Shop')
    print('x: Exit')
    option = input('Option: ').strip().lower()
    if option == 's':
        return option
    elif option == 'x':
        return option
    else:
        while option != 's' and option != 'x':
            option = input("Invalid (s/x): ").strip().lower()
    return option
def cart_menu():
    print('----CART MENU----')
    print('1:Cookie-$1.50')
    print('2:Sandwich-$4.00')
    print('3:Water-$1.00')
    item = int(input('Item: '))
    if item == 1:
        print('Added cookie')
        return item
    elif item == 2:
        print('Added sandwich')
        return item
    elif item == 3:
        print('Added water')
        return item
    else:
        while not (1 <= item <= 3):
            item = int(input('Invalid (1-3): '))
        if item == 1:
            print('Added cookie')
            return item
        elif item == 2:
            print('Added sandwich')
            return item
        elif item == 3:
            print('Added water')
            return item
def main():
    num_cookie = 0
    num_sandwich = 0
    num_water = 0
    cookie_cost = 0
    sandwich_cost = 0
    water_cost = 0
    while True:
        option = main_menu()
        if option == 's':
            cart_item = cart_menu()
            if cart_item == 1:
                num_cookie = num_cookie + 1
                cookie_cost = cookie_cost + 1.50
            elif cart_item == 2:
                num_sandwich = num_sandwich + 1
                sandwich_cost = sandwich_cost + 4.00
            else:
                num_water = num_water + 1
                water_cost = water_cost + 1.00
        else:
            total_cost = cookie_cost + sandwich_cost + water_cost
            print('-----------------------------------')
            print(f'({num_cookie}) - Cookie = ${cookie_cost:.2f}')
            print(f'({num_sandwich}) - Sandwich = ${sandwich_cost:.2f}')
            print(f'({num_water}) - Water = ${water_cost:.2f}')
            print('-----------------------------------')
            print(f'GRAND TOTAL = ${total_cost:.2f}')
            print('-----------------------------------')
            break
main()


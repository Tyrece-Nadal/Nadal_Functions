#display menu
def display_menu():
    print("Welcome to the food ordering system!")
    print("Here is the Menu!:")
    print("1. Sushi - P105.00)")
    print("2. Pizza - P150.00 ")
    print("3. Burger - P65.00")
    print("4. Taco - P85.00")
    print("5. Water - P15.00")
    print("6. Soda - P25.oo")
    
#get the prices of the items
def get_item_price(choice):
    menu_prices = {1: 105.00, 2: 150.00, 3: 65.00, 4: 85.00, 5: 15.00, 6:25.00}
    return menu_prices.get(choice, 0)

#calculate total and change 
def calculate_change(total, cash):
    return cash - total

display_menu()
choice  = int(input("Enter the number of the food that you would like to order:"))
price = get_item_price(choice)

if price ==0:
    print("INVALID CHOICE")
else:
    print(f"Your total is P{price:.2f}")
    while True:
        cash = float(input("Enter your payment:"))
        if cash >= price:
            change = calculate_change(price, cash)
            print(f"Thank you for your order! Your change is P{change:.2f}")
            break
        else: 
            print("Insufficient amount! Please try again and provide enough cash!")
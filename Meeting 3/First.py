menu_items = ["Pizza", "Burger", "Salad", "Pasta", "Juice"]
menu_prices = [8.5, 5.0, 4.5, 7.0, 2.5]

def show_menu(items, prices):
    print("\nMenu:")
    for i in range(len(items)):
        print(f"{i+1}. {items[i]} - ${prices[i]}")
    
def take_order(items):
    order = []
    count = 0
    
    while count < 3:
        choice = int(input("Enter item number: ")) - 1
        if 0 <= choice < len(items):
            order.append(choice)
            count += 1
        else:
            print("Invalid choice. Try again.")
    
    return order

def calculate_total(order, prices):
    total = sum(prices[i] for i in order)
    return total

while True:
    show_menu(menu_items, menu_prices)
    user_order = take_order(menu_items)
    total_price = calculate_total(user_order, menu_prices)

    print("\nYour order summary:")
    for i in user_order:
        print(f"- {menu_items[i]}: ${menu_prices[i]}")
    print(f"Total price: ${int(total_price)}")

    again = input("\nDo you want to order again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thank you for your order!")
        break

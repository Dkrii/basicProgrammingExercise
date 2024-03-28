def calculate_selling_price(cost_price):
    return cost_price * 1.1  # 10% markup

def display_items(items):
    print("\nAvailable Items:")
    for name, price, stock in items:
        print(f"{name}: ${price:.2f} - Stock: {stock}")

def make_transaction(items, name, quantity):
    for i, (item_name, price, stock) in enumerate(items):
        if item_name == name:
            if stock >= quantity:
                items[i] = (item_name, price, stock - quantity)
                return price * quantity
            else:
                print(f"Insufficient stock of {name}. Available stock: {stock}")
                return 0
    print(f"{name} not found.")
    return 0

def main():
    items = [("Lipstick", 10.0, 20), ("Eyeshadow", 15.0, 15), ("Foundation", 20.0, 10)]
    transactions = 0
    total_profit = 0.0

    while True:
        display_items(items)
        choice = input("\nEnter 'buy' to make a purchase or 'done' to finish: ").lower()

        if choice == 'done':
            break
        elif choice == 'buy':
            item_name = input("Enter the name of the item you want to buy: ")
            quantity = int(input("Enter the quantity: "))
            profit = make_transaction(items, item_name, quantity)
            if profit > 0:
                total_profit += profit
                transactions += 1
                print(f"Transaction successful! Total cost: ${profit:.2f}")
        else:
            print("Invalid choice. Please enter 'buy' or 'done'.")

    print(f"\nTotal transactions: {transactions}")
    print(f"Total profit: ${total_profit:.2f}")

if __name__ == "__main__":
    main()
products = {
    "101": ("Milk", 2.50),
    "102": ("Eggs", 3.00),
    "103": ("Bread", 1.75),
    "104": ("Cheese", 4.50),
    "105": ("Apple", 0.50)
}

cart = ["101", "105", "105", "999", "103", "105"]

def receipt_generator(carts, products):
    total = 0

    for idd in carts:
        if idd in products:
            name, price = products[idd]
            print(f"{name}: ${price:.2f}")
            total += price
        else:
            print(f"Item {idd} not found.")

    print('-' * 20)


    print(f"Grand Total: ${total:.2f}")
receipt_generator(cart, products)
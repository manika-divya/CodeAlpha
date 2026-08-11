cart = []

# To add product
def add_product():
    product = input('Enter product name: ')
    price = float(input('Enter product price: '))
    cart.append([product,price])
    print('Product added successfully!\n')


# To display everything inside the cart
def view_cart():
    if not cart:
        print('Your cart is empty.\n')
        return
    total =0
    print('\n-----SHOPPING CART-----')
    for i ,item in enumerate (cart,start = 1):
        print(f"{i}. {item[0]} -Rs{item[1]:.2f}")
        total += item[1]
    print(f"Total Bill: Rs{total:.2f}\n")

#To allow the user to remove something from cart
def remove_product():
    product = input('Enter product name to remove: ')
    for item in cart:
        if item[0].lower() == product.lower():
            cart.remove(item)
            print(f"Product removed successfully!\n")
            return
    print('Product not found.\n')


#Menu that lets the user choose what to do
while True:
    print('-----SHOPPING CART SYSTEM-----')
    print('1. Add product')
    print('2. View Cart')
    print('3. Remove Product')
    print('4. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        add_product()
    elif choice == '2':
        view_cart()
    elif choice == '3':
        remove_product()
    elif choice == '4':
        print('Thank You for shopping')
        break
    else:
        print('Invalid choice. Please try again.\n')
    
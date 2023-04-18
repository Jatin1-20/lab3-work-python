# Initialize an empty dictionary to store products and brands
shoppingCart = {}

# Menu-driven program to add or delete products from the shopping cart
while True:
    print("WELCOME TO THE AMANDO SHOPPING SITE\n")
    print("1. Add product to the cart.")
    print("2. Search the product.")
    print("3. Delete the product from the cart.")
    print("4. Quit.\n")

    # Get user's choice
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        # Add a new product to the shopping cart
         n = int(input("Enter the number of items to be added in the stationary shop: "))
         if len(shoppingCart) + n > 5:
            print("Cart is full.")
         else:
          for i in range(n):
                item = input("Enter an item: ")
                brand = input("Enter the brand name: ")
                shoppingCart[item] = brand

          print("You added the following items to the cart:")
          for item, brand in shoppingCart.items():
                print(item + ": " + brand)


    elif choice == '2':
        # Search for a product in the shopping cart
         product_name = input("Enter the item name to search: ")
         if product_name in shoppingCart:
            print("Product Name:", product_name, ", Brand:", shoppingCart[product_name])
         else:
            print("No product exists with this name")
   
    elif choice == '3':
        # Delete a product from the shopping cart
        if len(shoppingCart) != 0:
            product_name = input("Enter the item name to be deleted: ")
            if product_name in shoppingCart:
                del shoppingCart[product_name]
                print("Product deleted from the cart.\n")
            else:
                print("No product exists with this name.\n")
        else:
            print("Cart is empty, no item is found.\n")

    elif choice == '4':
        # Quit the program
        print("Thanks for shopping with us!")
        break

    else:
        # Invalid choice
        print("Wrong option Entered. Please enter 1/2/3/4.\n")

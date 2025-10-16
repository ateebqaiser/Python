#TASK 1: Create a dictionary named store_items that contains item names as keys and their prices as values
store_items = {
    "Rice": 150,
    "Sugar": 120,
    "Milk": 90,
    "Bread": 80,
    "Eggs": 200
}

# Display all items in a formatted list using a loop
print("Available Items in Store:")
for item, price in store_items.items():
    print(f"{item}: Rs {price}")

# TASK 2:
# Create a function named calculate_bill(cart) that:
# Takes a dictionary cart with item names as keys and quantities as values
# Calculates the total bill using a loop
# Applies a 10% discount if the total exceeds 500
# Returns the final amount
def calculate_bill(cart):
    total = 0
    for item, qty in cart.items():
        total += store_items[item] * qty
    return total

#TASK 3: Use if-else statements to check whether the item entered by the user exists in the store
# Keep asking the user to add items to the cart until they type 'done'
cart = {}
while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item == "done":  # Exit loop when user is finished
        break
    if item in store_items:  # Check if item exists in store
        qty = int(input("Enter quantity: "))
        cart[item] = qty  # Add item and quantity to cart
    else:
        print("Item not found! Please try again.")  # Invalid item message

#TASK 4: Finally, print the detailed bill showing each item, quantity, price, and total
bill = calculate_bill(cart)

# Apply discount if applicable
if bill > 500:
    discount = bill * 0.10
    bill -= discount
    print(f"\n10% discount applied! You saved Rs {discount}")

# Display final total
print(f"\nYour Total Bill: Rs {bill}")

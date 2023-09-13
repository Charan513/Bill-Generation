
# Import Packages

from datetime import datetime

# Code
def main():
    name = input("Enter Your Name: ")

    # List Menu Items
    menu_items = """
            Menu Items

    Rice            RS 45/kg
    Sugar           RS 30/kg
    Mushroom        RS 50/pack 
    Apples          RS 100/kg
    Biriyani Rice   RS 60/kg
    White           RS 35/kg
    Avacado         RS 600/kg
    Airel Wash      RS 250
    Dragan Fruit    RS 200/kg
    Onions          RS 25/kg

    """

    # Declaration
    price = 0
    cart_list = []
    total_price = 0
    item_list = []
    quantity_list = []
    price_list = []

    # Rates for Items
    items = {
        "Rice": 45,
        "Sugar": 30,
        "Mushroom": 50,
        "Apples": 100,
        "Biriyani Rice": 60,
        "White": 35,
        "Avacado": 600,
        "Airel Wash": 250,
        "Dragan Fruit": 200,
        "Onions": 25
    }

    print(menu_items)
    
    for i in range(len(menu_items)):
        input1 = int(input("Enter 1 to buy an item, 2 to exit: "))
        if input1 == 2:
            break
        if input1 == 1:
            item = input("Enter Item you want: ")
            quantity = float(input("Enter item quantity: "))
            if item in items.keys():
                price = quantity * (items[item])
                cart_list.append((item, quantity, items, price))
                total_price += price
                # Limit item name to 20 characters or less
                item = item[:20]
                item_list.append(item)
                quantity_list.append(quantity)
                price_list.append(price)
                gst = (total_price * 5) / 100
                final_amount = gst + total_price
            else:
                print("Item you entered is not available..")
        else:
            print("You entered wrong number..")
        bill = input("To Generate Bill Enter Yes/No: ")
        if bill == "Yes":
            # pass
            if final_amount != 0:
                print(32 * "=", "V Mart", 35 * "=")
                print(32 * " ", "Nandyal \n")
                print("Name:", name.ljust(30), 5 * " ", "Date:", datetime.now())
                print(75 * "-")
                print("Serial No", 8 * " ", "Items", 20 * " ", "Quantity", 13 * " ", "Price")

                for i in range(len(cart_list)):
                    formatted_item = item_list[i].ljust(20)  # Pad the item name with spaces to make it 20 characters wide
                    print(i, 16 * " ", formatted_item, 8 * " ", quantity_list[i], 15 * " ", price_list[i])

                print(75 * "-")
                print(50 * " ", "Total Amount: Rs ", total_price)
                print("GST Amount:", 52 * " ", "Rs ", gst)
                print(75 * "-")
                print(50 * " ", "Final Amount: Rs ", final_amount)
                print(75 * "-")
                print(25 * " ", "Thanks for visiting ....")
                print(75 * "-")


if __name__ == "__main__":
    main()



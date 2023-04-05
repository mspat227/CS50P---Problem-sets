items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price = 0

while True:
    try:
        #get the user input with title function as the dict items are in capital first letters 
        user_input = input("Item: ").title()

        #check if the user input is in the dict
        if user_input in items:
            #if the otem contains user input plus the price with item price and print total
            price += items[user_input]
            print(f"Total: ${price:.2f}")
        else:
            #if user input not in dict the raise keyerror and pass the error below 
            raise KeyError

    except(KeyError):
        pass
    #if user press clt-d then print total and break the program
    except(EOFError):
        print(f"\nTotal: ${price:.2f}")
        break
            
            

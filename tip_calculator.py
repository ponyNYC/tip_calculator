# Tip calculator intro
print('\nWelcome to the Easy Peasy Tip Calculator!\n')

# Start of loop for customer to start over
while True:
    
    # Total of bill
    while True:
        try:
            user_input = float(input("What was the total bill?\n $"))
            food_total = float(user_input)
            break 
        except ValueError:
            print("I'm sorry, looks like you typed something incorrectly. Please try typing in a number!\n")

    # Total of bill + sales tax
    sales_tax = .1 * food_total
  
    # Tip amount
    tip = float(input("What percentage Tip would you like to give? \n "))

    # Total of bill + tip amount calculated
    tip_amount = (food_total * tip) / 100
    grand_total = food_total + sales_tax + tip_amount
    print(f'The total bill including sales tax and tip is: {grand_total}\n')

    # Number of guests
    guests = int(input("How many guests are in the party?\n "))

    # Amount per guest
    share = "{:.2f}".format(grand_total / guests)
    print(f"Each guest should pay: ${share}\n")

    # Option to submit new parameters
    if input('Would you like to restart? Enter "Y" for yes and "N" for no: \n') == "Y":
        continue

    # Exit tip calculator
    print('Thank you for using the Easy Peasy Tip Calculator!\n')
    break
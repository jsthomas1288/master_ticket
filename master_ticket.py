service_charge = 2
TICKET_PRICE = 10
tickets_remaining = 100

name = input("What is your name?   ").capitalize()

def calc_price(num_of_tickets):
    return (num_of_tickets * TICKET_PRICE) + service_charge

while tickets_remaining > 0:
    print("There are {} tickets remaining.".format(tickets_remaining))
    try:
        try:
            num_of_tickets = int(input("Hello, {} how many tickets would you like to buy?   ".format(name)))
        except ValueError:
            raise ValueError("Please enter a whole number when purchasing tickets")
        else:
            if num_of_tickets > tickets_remaining:
                raise ValueError("There are {} tickets left".format(tickets_remaining))
    except ValueError as err:
        print("That's an incorrect value. {}. Please try again!".format(err))
    else:
        total = calc_price(num_of_tickets)
        proceed = input("Would you like to proceed? (Yes/No)   ")
        if proceed.lower() == "yes":
            # TODO: Gather credit card information and process it
            tickets_remaining -= num_of_tickets
            print("SOLD!")
            print("Your total is ${}.".format(total))   
            print("There are now {} tickets remaining.".format(tickets_remaining))
        else:
            print("Thanks anyways {}!".format(name))

    if tickets_remaining == 0:
        print("We're all sold out! There are no more remaining tickets!")

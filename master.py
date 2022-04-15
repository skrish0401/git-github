SERVICE_CHARGE=2
TICKET_PRICE=10
tickets_remaining=100

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} remaining for sale..".format(tickets_remaining))
    name=input("What Is Your Name   ?   ")
    number_of_tickets=input("How Many Tickets Would You Like {} ".format(name))
    try:
        number_of_tickets=int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh No We ran into an Issue. {}. Please Try Again".format(err))
    else:
        amount=calculate_price(number_of_tickets)
        print("Total Due is ${}".format(amount))
        confirm=input("{} do you want to purchase the tickets ?   Y/N  ".format(name))
        if confirm.lower() == "y":
            print("SOLD!!")
            tickets_remaining -=number_of_tickets
            print(tickets_remaining)
        else:
            print("Thank You Anyways {}".format(name))
            exit()
print("Sorry All The Tickets are Sold Out !!!!")

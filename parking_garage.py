class ParkingGarage:
    def __init__(self, tickets, parking_spaces):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = {}

    def take_ticket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            self.parking_spaces.pop(0)
            self.current_ticket = {'ticket_number': ticket_number, 'paid': False}
            print(f"Your ticket number is {ticket_number}. Please keep it safe.")
        else:
            print("Sorry, the garage is full. Please come back later.")

    def pay_for_parking(self):
        if self.current_ticket:
            if self.current_ticket['paid']:
                print("Your ticket has already been paid. You have 15 minutes to leave.")
            else:
                payment = input("Please enter the amount to pay: ")
                if payment:
                    self.current_ticket['paid'] = True
                    print("Payment successful. Your ticket has been paid.")
                else:
                    print("Payment unsuccessful. Please try again.")
        else:
            print("No ticket to pay. Please take a ticket first.")

    def leave_garage(self):
        if self.current_ticket:
            if self.current_ticket['paid']:
                print("Thank you for visiting. Have a nice day!")
                self.tickets.append(self.current_ticket['ticket_number'])
                self.parking_spaces.append(self.current_ticket['ticket_number'])
                self.current_ticket = {}
            else:
                payment = input("Please pay the ticket before leaving: ")
                if payment:
                    self.current_ticket['paid'] = True
                    print("Payment successful. Thank you for visiting. Have a nice day!")
                    self.tickets.append(self.current_ticket['ticket_number'])
                    self.parking_spaces.append(self.current_ticket['ticket_number'])
                    self.current_ticket = {}
                else:
                    print("Payment unsuccessful. Please pay the ticket before leaving.")
        else:
            print("No ticket to leave. Please take a ticket first.")


tickets = [1, 2, 3, 4, 5]  
parking_spaces = [1, 2, 3, 4, 5] 
garage = ParkingGarage(tickets, parking_spaces)

while True:
    print("1. Take a ticket")
    print("2. Pay for parking")
    print("3. Leave the garage")
    print("4. Exit")
    
    choice = input("Please select an option: ")
    
    if choice == "1":
        garage.take_ticket()
    elif choice == "2":
        garage.pay_for_parking()
    elif choice == "3":
        garage.leave_garage()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
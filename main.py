TOTAL_SEATS = 50
available_seats = list(range(1, TOTAL_SEATS + 1))
bookings = {}

def check_availability():
    print("Available Seats:", len(available_seats))
    print("Seat Numbers:", available_seats)

import random

def book_ticket():
    if len(available_seats) == 0:
        print("No seats available!")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    seat = available_seats.pop(0)  # take first available seat
    booking_id = str(random.randint(1000, 9999))

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat
    }

    print("\nTicket Booked Successfully!")
    print("Booking ID:", booking_id)
    print("Seat Number:", seat)

def menu():
    while True:
        print("\n===== Railway Reservation System =====")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            check_availability()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            print("Coming soon...")
        elif choice == "4":
            print("Coming soon...")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

menu()

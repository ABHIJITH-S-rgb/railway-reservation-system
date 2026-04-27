TOTAL_SEATS = 50
available_seats = list(range(1, TOTAL_SEATS + 1))
bookings = {}

def check_availability():
    print("Available Seats:", len(available_seats))
    print("Seat Numbers:", available_seats)

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
            print("Coming soon...")
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

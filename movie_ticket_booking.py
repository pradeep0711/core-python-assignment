print("======MOVIE TICKET BOOKING SYSTEM======")
def book_seat(total_seats, booked_seats, seat):
    if seat not in booked_seats and seat <= total_seats:
        booked_seats.append(seat)
        print(f"Seat no {seat} booked successfully!")
        booked_seats.sort()
    else:
        print("Seat already booked or invalid seat number.")

def cancel_seat(booked_seats, seat):
    if seat in booked_seats:
        booked_seats.remove(seat)
        print(f"Seat no {seat} cancelled successfully!")
    else:
        print("Seat not found.")

def available_seats(total_seats, booked_seats):
    return [i for i in range(1, total_seats + 1) if i not in booked_seats]


total_seats = int(input("Enter total number of seats: "))
booked_seats = list(map(int, input("Enter booked seats (comma-separated): ").split(',')))
while True:
    action = input("Do you want to book or cancel a seat? (book/cancel/exit): ").lower()
    if action == 'exit':
        break
    seat = int(input("Enter seat number: "))
    if action == 'book':
        book_seat(total_seats, booked_seats, seat)
    elif action == 'cancel':
        cancel_seat(booked_seats, seat)
    else:
        print("Invalid action.")
    print("Available seats:", available_seats(total_seats, booked_seats))

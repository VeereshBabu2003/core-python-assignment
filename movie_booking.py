def book_seat(booked_seats, seat, total_seats=10):
    """Books a seat if available."""
    if seat in booked_seats:
        return "Seat already booked."
    booked_seats.append(seat)
    return booked_seats

def cancel_seat(booked_seats, seat):
    """Cancels a booked seat."""
    if seat in booked_seats:
        booked_seats.remove(seat)
    return booked_seats

def available_seats(booked_seats, total_seats=10):
    """Returns a list of available seats."""
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

# Example Input
booked = [2, 5, 7]
booked = book_seat(booked, 3)
booked = cancel_seat(booked, 5)

print("Available seats:", available_seats(booked))

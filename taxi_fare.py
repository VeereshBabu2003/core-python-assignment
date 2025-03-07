def calculate_fare(trips):
    """Calculates taxi fare for multiple trips."""
    base_fare = 50
    distance_fare = 10
    fares = [base_fare + distance_fare * trip for trip in trips]
    
    total_fare = sum(fares)
    
    for i, fare in enumerate(fares, 1):
        print(f"Trip {i}: ${fare}")

    print(f"Total Fare: ${total_fare}")

# Example Input
trips = [5, 10, 3]
calculate_fare(trips)

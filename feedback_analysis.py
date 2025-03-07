def calculate_positive_feedback(ratings):
    """Calculates the percentage of positive feedback (ratings 4 or 5)."""
    if not ratings:
        return "No ratings available."
    
    positive = sum(1 for r in ratings if r >= 4)
    percentage = (positive / len(ratings)) * 100
    return f"Positive Feedback: {percentage:.2f}%"

# Example Input
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(calculate_positive_feedback(ratings))

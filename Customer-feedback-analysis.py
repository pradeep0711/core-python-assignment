def calculate_positive_feedback_percentage(ratings):
    if not ratings:
        return 0
    positive_count = sum(1 for rating in ratings if rating >= 4)
    return (positive_count / len(ratings)) * 100

def get_ratings_from_user():
    return list(map(int, input("Enter ratings (space-separated): ").split()))

def display_positive_feedback(percentage):
    if percentage > 0:
        print(f"Positive Feedback: {percentage:.2f}%")
    else:
        print("No ratings available.")
ratings = get_ratings_from_user()
percentage = calculate_positive_feedback_percentage(ratings)
display_positive_feedback(percentage)

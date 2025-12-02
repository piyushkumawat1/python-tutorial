# Weekly Fitness Tracking Analyzer

def get_valid_number(prompt):
    """Ensures user enters a non-negative numeric value."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Value cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Enter a numeric value.")

def collect_weekly_data():
    """Collects steps, calories, and sleep hours for 7 days."""
    data = {
        "steps": [],
        "calories": [],
        "sleep": []
    }

    print("\nEnter your 7-day fitness data:\n")
    for day in range(1, 8):
        print(f"--- Day {day} ---")
        steps = get_valid_number("Steps walked: ")
        calories = get_valid_number("Calories burned: ")
        sleep = get_valid_number("Hours of sleep: ")

        data["steps"].append(steps)
        data["calories"].append(calories)
        data["sleep"].append(sleep)

    return data

def analyze_data(data):
    """Calculates averages, max, and min values for the week."""
    analysis = {}
    for key in data:
        values = data[key]
        analysis[key] = {
            "average": sum(values) / 7,
            "max": max(values),
            "min": min(values)
        }
    return analysis

def give_recommendations(analysis):
    """Provides improvement suggestions based on weekly averages."""
    print("\n=== Improvement Suggestions ===")

    # Steps recommendation
    if analysis["steps"]["average"] < 8000:
        print("- Try walking at least 8,000 steps daily to improve health.")
    else:
        print("- Great job! Your daily step average is healthy.")

    # Calories recommendation (assuming workouts)
    if analysis["calories"]["average"] < 300:
        print("- Try burning at least 300+ calories daily through light exercise.")
    else:
        print("- Strong effort! You are burning good calories.")

    # Sleep recommendation
    if analysis["sleep"]["average"] < 7:
        print("- Aim for 7–8 hours of sleep for better recovery.")
    else:
        print("- Excellent! Your sleep duration is healthy.")

def display_report(analysis):
    """Prints a formatted weekly report."""
    print("\n===== WEEKLY FITNESS REPORT =====\n")
    for category, stats in analysis.items():
        print(f"{category.capitalize()}:")
        print(f"  Average: {stats['average']:.2f}")
        print(f"  Max: {stats['max']}")
        print(f"  Min: {stats['min']}\n")

def main():
    print("=== FITNESS TRACKING ANALYZER ===")
    data = collect_weekly_data()

    # Ensure 7 days of data
    if len(data["steps"]) != 7:
        print("Error: Data for 7 days is required!")
        return

    analysis = analyze_data(data)
    display_report(analysis)
    give_recommendations(analysis)

# Run the program
main()

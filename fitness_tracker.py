"""
Fitness Tracker - Python Mini Project
B.Tech Sem 3-4 | Programming in Python
"""

import json
import os
from datetime import datetime, date


DATA_FILE = "fitness_data.json"


def load_data():
    """Load existing fitness data from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"users": {}, "workouts": [], "goals": {}}


def save_data(data):
    """Save fitness data to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def register_user(data):
    """Register a new user profile."""
    print("\n--- Register User ---")
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))

    bmi = weight / ((height / 100) ** 2)
    bmi_category = (
        "Underweight" if bmi < 18.5 else
        "Normal" if bmi < 25 else
        "Overweight" if bmi < 30 else
        "Obese"
    )

    data["users"][name] = {
        "age": age,
        "weight": weight,
        "height": height,
        "bmi": round(bmi, 2),
        "bmi_category": bmi_category,
        "registered": str(date.today())
    }
    save_data(data)
    print(f"\n✅ User '{name}' registered! BMI: {bmi:.2f} ({bmi_category})")
    return name


def log_workout(data, user):
    """Log a workout session."""
    print("\n--- Log Workout ---")
    print("Workout types: Running, Cycling, Swimming, Gym, Yoga, Walking")
    workout_type = input("Enter workout type: ").strip()
    duration = int(input("Duration (minutes): "))
    calories = int(input("Calories burned: "))
    notes = input("Notes (optional): ").strip()

    entry = {
        "user": user,
        "date": str(date.today()),
        "time": datetime.now().strftime("%H:%M"),
        "type": workout_type,
        "duration_min": duration,
        "calories": calories,
        "notes": notes
    }
    data["workouts"].append(entry)
    save_data(data)
    print(f"\n✅ Workout logged: {workout_type} for {duration} mins, {calories} kcal burned.")


def set_goal(data, user):
    """Set weekly fitness goals."""
    print("\n--- Set Weekly Goal ---")
    weekly_workouts = int(input("Target workouts per week: "))
    weekly_calories = int(input("Target calories to burn per week: "))

    data["goals"][user] = {
        "weekly_workouts": weekly_workouts,
        "weekly_calories": weekly_calories
    }
    save_data(data)
    print(f"\n✅ Goals set: {weekly_workouts} workouts/week, {weekly_calories} kcal/week.")


def view_progress(data, user):
    """View weekly progress and goal achievement."""
    print(f"\n--- Progress Report for {user} ---")

    today = date.today()
    week_start = today.toordinal() - today.weekday()
    week_workouts = [
        w for w in data["workouts"]
        if w["user"] == user and
        date.fromisoformat(w["date"]).toordinal() >= week_start
    ]

    total_sessions = len(week_workouts)
    total_calories = sum(w["calories"] for w in week_workouts)
    total_duration = sum(w["duration_min"] for w in week_workouts)

    print(f"\n📅 This Week:")
    print(f"   Workout Sessions : {total_sessions}")
    print(f"   Total Duration   : {total_duration} minutes")
    print(f"   Calories Burned  : {total_calories} kcal")

    if user in data["goals"]:
        g = data["goals"][user]
        workout_pct = min(100, (total_sessions / g["weekly_workouts"]) * 100)
        calorie_pct = min(100, (total_calories / g["weekly_calories"]) * 100)
        print(f"\n🎯 Goal Progress:")
        print(f"   Workouts : {total_sessions}/{g['weekly_workouts']} ({workout_pct:.0f}%)")
        print(f"   Calories : {total_calories}/{g['weekly_calories']} kcal ({calorie_pct:.0f}%)")

    if week_workouts:
        print(f"\n📋 Workout Log:")
        for w in week_workouts:
            print(f"   {w['date']} | {w['type']:10s} | {w['duration_min']} min | {w['calories']} kcal")


def view_history(data, user):
    """View full workout history for a user."""
    print(f"\n--- Full History for {user} ---")
    history = [w for w in data["workouts"] if w["user"] == user]
    if not history:
        print("No workouts recorded yet.")
        return
    for w in history[-10:]:  # Show last 10
        print(f"  {w['date']} | {w['type']:10s} | {w['duration_min']} min | {w['calories']} kcal | {w['notes']}")


def calorie_calculator():
    """Estimate calories burned by activity and body weight."""
    print("\n--- Calorie Calculator ---")
    weight = float(input("Your weight (kg): "))
    duration = int(input("Duration (minutes): "))
    print("Activities: 1-Running  2-Cycling  3-Swimming  4-Walking  5-Yoga")
    choice = input("Choose activity (1-5): ")

    met_values = {"1": 9.8, "2": 7.5, "3": 8.0, "4": 3.8, "5": 3.0}
    activity_names = {"1": "Running", "2": "Cycling", "3": "Swimming", "4": "Walking", "5": "Yoga"}

    met = met_values.get(choice, 5.0)
    calories = (met * weight * duration) / 60
    print(f"\n🔥 Estimated calories burned ({activity_names.get(choice, 'Activity')}): {calories:.0f} kcal")


def bmi_calculator():
    """Standalone BMI calculator."""
    print("\n--- BMI Calculator ---")
    weight = float(input("Weight (kg): "))
    height = float(input("Height (cm): "))
    bmi = weight / ((height / 100) ** 2)
    category = (
        "Underweight" if bmi < 18.5 else
        "Normal weight" if bmi < 25 else
        "Overweight" if bmi < 30 else
        "Obese"
    )
    print(f"\n📊 BMI: {bmi:.2f} — {category}")
    print("   Healthy BMI range: 18.5 – 24.9")


def main():
    """Main application loop."""
    data = load_data()
    current_user = None

    print("=" * 45)
    print("       🏋️  FITNESS TRACKER  🏋️")
    print("   Python Mini Project | B.Tech Sem 3-4")
    print("=" * 45)

    while True:
        print("\n====== MAIN MENU ======")
        if current_user:
            print(f"  Logged in as: {current_user}")
        print("  1. Register / Switch User")
        print("  2. Log Workout")
        print("  3. Set Weekly Goal")
        print("  4. View Weekly Progress")
        print("  5. View Workout History")
        print("  6. Calorie Calculator")
        print("  7. BMI Calculator")
        print("  8. Exit")
        print("=======================")

        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            if data["users"]:
                print("\nExisting users:", ", ".join(data["users"].keys()))
                sel = input("Enter name to login or press Enter to register new: ").strip()
                if sel in data["users"]:
                    current_user = sel
                    u = data["users"][sel]
                    print(f"✅ Welcome back, {sel}! BMI: {u['bmi']} ({u['bmi_category']})")
                else:
                    current_user = register_user(data)
            else:
                current_user = register_user(data)

        elif choice == "2":
            if not current_user:
                print("⚠️  Please register/login first (Option 1).")
            else:
                log_workout(data, current_user)

        elif choice == "3":
            if not current_user:
                print("⚠️  Please register/login first.")
            else:
                set_goal(data, current_user)

        elif choice == "4":
            if not current_user:
                print("⚠️  Please register/login first.")
            else:
                view_progress(data, current_user)

        elif choice == "5":
            if not current_user:
                print("⚠️  Please register/login first.")
            else:
                view_history(data, current_user)

        elif choice == "6":
            calorie_calculator()

        elif choice == "7":
            bmi_calculator()

        elif choice == "8":
            print("\n👋 Thank you for using Fitness Tracker! Stay Fit!")
            break

        else:
            print("❌ Invalid choice. Please enter 1-8.")


if __name__ == "__main__":
    main()
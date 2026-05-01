# 🏋️ Fitness Tracker 

A command-line Fitness Tracker application built entirely in Python that helps users log workouts, track weekly progress against goals, calculate BMI, and estimate calorie burn.

---

## 📋 Features

| Feature | Description |
|---|---|
| 👤 User Profile | Register with age, weight, height; auto-calculates BMI |
| 🏃 Workout Logger | Log type, duration, calories, and notes for each session |
| 🎯 Goal Tracker | Set weekly workout & calorie targets |
| 📊 Progress Report | View this week's sessions vs goals |
| 📅 History | View last 10 workout entries |
| 🔥 Calorie Calculator | Estimate calories burned using MET formula |
| 📐 BMI Calculator | Standalone BMI tool with category classification |

---

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Libraries:** `json`, `os`, `datetime` (all standard library — no pip install needed)
- **Storage:** JSON file (`fitness_data.json`) for persistent local data

---

## 🚀 How to Run

### Prerequisites
- Python 3.6 or above

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/your-username/fitness-tracker.git

# 2. Navigate to the folder
cd fitness-tracker

# 3. Run the application
python fitness_tracker.py
```

No external libraries required — runs out of the box!

---

## 🧪 Run Tests

```bash
python -m pytest test_fitness_tracker.py -v
# or
python test_fitness_tracker.py
```

---

## 📁 Project Structure

```
fitness-tracker/
│
├── fitness_tracker.py        # Main application
├── test_fitness_tracker.py   # Unit tests
├── fitness_data.json         # Auto-created on first run (data store)
└── README.md                 # Project documentation
```

---

## 📐 Calorie Formula (MET-based)

```
Calories = (MET × Weight_kg × Duration_min) / 60
```

MET values used:
- Running: 9.8
- Cycling: 7.5
- Swimming: 8.0
- Walking: 3.8
- Yoga: 3.0

---

## 📊 BMI Categories

| BMI Range | Category |
|---|---|
| < 18.5 | Underweight |
| 18.5 – 24.9 | Normal weight |
| 25.0 – 29.9 | Overweight |
| ≥ 30.0 | Obese |

---

## 🌱 Mapped SDG

**SDG 3 — Good Health and Well-Being**: This project promotes physical fitness awareness by helping users track exercise habits and health metrics.

---

## 👨‍💻 Author - Saurabh

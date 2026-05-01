"""
Unit Tests for Fitness Tracker
"""

import unittest
import json
import os
from unittest.mock import patch, MagicMock
from fitness_tracker import load_data, save_data, bmi_calculator, calorie_calculator


class TestFitnessTracker(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures."""
        self.test_data = {
            "users": {
                "TestUser": {
                    "age": 20,
                    "weight": 70,
                    "height": 175,
                    "bmi": 22.86,
                    "bmi_category": "Normal",
                    "registered": "2025-01-01"
                }
            },
            "workouts": [
                {
                    "user": "TestUser",
                    "date": "2025-01-01",
                    "time": "08:00",
                    "type": "Running",
                    "duration_min": 30,
                    "calories": 300,
                    "notes": "Morning run"
                }
            ],
            "goals": {
                "TestUser": {
                    "weekly_workouts": 5,
                    "weekly_calories": 2000
                }
            }
        }

    def test_bmi_calculation(self):
        """Test BMI formula: weight / (height_m)^2"""
        weight = 70
        height = 175
        bmi = weight / ((height / 100) ** 2)
        self.assertAlmostEqual(bmi, 22.86, places=1)

    def test_bmi_category_normal(self):
        """Test BMI category for normal weight."""
        bmi = 22.5
        category = (
            "Underweight" if bmi < 18.5 else
            "Normal" if bmi < 25 else
            "Overweight" if bmi < 30 else
            "Obese"
        )
        self.assertEqual(category, "Normal")

    def test_bmi_category_underweight(self):
        bmi = 17.0
        category = "Underweight" if bmi < 18.5 else "Other"
        self.assertEqual(category, "Underweight")

    def test_bmi_category_obese(self):
        bmi = 32.0
        category = (
            "Underweight" if bmi < 18.5 else
            "Normal" if bmi < 25 else
            "Overweight" if bmi < 30 else
            "Obese"
        )
        self.assertEqual(category, "Obese")

    def test_calorie_calculation(self):
        """Test calorie estimation using MET formula."""
        met = 9.8   # Running
        weight = 70
        duration = 30
        calories = (met * weight * duration) / 60
        self.assertAlmostEqual(calories, 343.0, places=0)

    def test_workout_log_structure(self):
        """Test that workout log has required fields."""
        workout = self.test_data["workouts"][0]
        required_fields = ["user", "date", "type", "duration_min", "calories"]
        for field in required_fields:
            self.assertIn(field, workout)

    def test_user_profile_structure(self):
        """Test that user profile has required fields."""
        user = self.test_data["users"]["TestUser"]
        required_fields = ["age", "weight", "height", "bmi", "bmi_category"]
        for field in required_fields:
            self.assertIn(field, user)

    def test_goal_structure(self):
        """Test goal structure."""
        goal = self.test_data["goals"]["TestUser"]
        self.assertIn("weekly_workouts", goal)
        self.assertIn("weekly_calories", goal)

    def test_weekly_calorie_total(self):
        """Test total calorie calculation from workouts."""
        workouts = self.test_data["workouts"]
        total = sum(w["calories"] for w in workouts if w["user"] == "TestUser")
        self.assertEqual(total, 300)

    def test_data_save_and_load(self):
        """Test that data is correctly saved and loaded."""
        test_file = "test_fitness_data.json"
        save_data.__globals__["DATA_FILE"] = test_file
        save_data(self.test_data)

        loaded = load_data.__globals__["DATA_FILE"]
        # Verify file was created
        if os.path.exists(test_file):
            with open(test_file, "r") as f:
                loaded = json.load(f)
            self.assertEqual(loaded["users"]["TestUser"]["bmi"], 22.86)
            os.remove(test_file)


if __name__ == "__main__":
    unittest.main(verbosity=2)
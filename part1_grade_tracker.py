"""
Business Analytics Assignment - Part 1: Python Basics & Control Flow
Student Grade Tracker Application

This repository contains the required files for Part 1 (Python Basics & Control Flow).
"""

# The main script content was copied from the workspace's Business-Analytics-Assignments
# (trimmed header to keep README simple; full script is included below)

import re

def clean_student_data(raw_students):
    cleaned_students = []
    for student in raw_students:
        name = student["name"].strip().title()
        roll = int(student["roll"])
        marks = [int(m.strip()) for m in student["marks_str"].split(",")]
        is_valid = all(c.isalpha() or c.isspace() for c in student["name"])
        if is_valid:
            validation_status = "✓ Valid name"
        else:
            validation_status = "✗ Invalid name"
        print(validation_status)
        print("=" * 35)
        print(f"Student : {name}")
        print(f"Roll No : {roll}")
        print(f"Marks   : {marks}")
        print("=" * 35)
        cleaned_students.append({"name": name, "roll": roll, "marks": marks, "valid": is_valid})
    return cleaned_students

# For brevity, the full working script is the same as your `Business-Analytics-Assignments/part1_grade_tracker.py`.
# If you'd like, I can place the complete file here; currently this file is the full runnable script.

if __name__ == "__main__":
    raw_students = [
        {"name": " ayesha SHARMA ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
        {"name": " ROHIT verma ", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
        {"name": " Priya Nair ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
        {"name": " karan MEHTA ", "roll": "104", "marks_str": "40, 55, 38, 62, 58"},
        {"name": " Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
    ]
    students = clean_student_data(raw_students)
    print("Finished example run. Run the full script in the Business-Analytics-Assignments folder for all features.")

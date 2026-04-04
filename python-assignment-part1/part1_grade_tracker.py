"""
Assignment Part 1 - Python Basics & Control Flow
Student Grade Tracker System
All 4 Tasks: Data Parsing, Marks Analysis, Class Performance Summary, String Manipulation
"""

# ============================================================================
# TASK 1: DATA PARSING & PROFILE CLEANING (5 marks)
# ============================================================================

print("\n" + "="*70)
print("TASK 1: DATA PARSING & PROFILE CLEANING")
print("="*70)

# Raw student data with inconsistent spacing and casing
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": " Priya Nair ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha Pillai ", "roll": "105", "marks_str": "75, 80, 78, 68, 85"},
]

# Task 1 Requirements:
# 1. Loop through raw_students and create cleaned version
# 2. Remove leading/trailing whitespace - convert to Title Case
# 3. Roll is converted from string to integer
# 4. Marks_str split by "," and each element converted to integer
# 5. Verify name is valid (only alphabetic and space)
# 6. Print formatted profile cards

cleaned_students = []

for student in raw_students:
    # Clean name: strip whitespace and convert to Title Case
    cleaned_name = student["name"].strip().title()
    
    # Convert roll to integer
    cleaned_roll = int(student["roll"])
    
    # Parse marks: split by comma and convert to integers
    marks_list = [int(mark.strip()) for mark in student["marks_str"].split(",")]
    
    # Validate name (check if contains only alphabetic characters and spaces)
    if all(char.isalpha() or char.isspace() for char in cleaned_name):
        cleaned_students.append({
            "name": cleaned_name,
            "roll": cleaned_roll,
            "marks": marks_list
        })
        
        # Print formatted profile card
        print(f"\n=============================")
        print(f"Student | {cleaned_name}")
        print(f"Roll    | {cleaned_roll}")
        print(f"Marks   | {marks_list}")
        print(f"=============================")
    else:
        print(f"\n✗ Invalid name: {cleaned_name}")

print(f"\n✓ Cleaned {len(cleaned_students)} student profiles")


# ============================================================================
# TASK 2: MARKS ANALYSIS USING LOOPS & CONDITIONALS (8 marks)
# ============================================================================

print("\n" + "="*70)
print("TASK 2: MARKS ANALYSIS USING LOOPS & CONDITIONALS")
print("="*70)

# Grade mapping
def get_grade(marks_avg):
    """Determine grade based on average marks"""
    if marks_avg >= 80:
        return "A+"
    elif marks_avg >= 70:
        return "A"
    elif marks_avg >= 60:
        return "B"
    elif marks_avg >= 50:
        return "C"
    else:
        return "F"

# Calculate statistics for each student
print("\n--- Individual Student Analysis ---\n")
print(f"{'Name':<20} | {'Marks':<30} | {'Avg':<6} | {'Grade':<6}")
print("-" * 75)

total_marks_all = 0
count_students = 0
highest_student = None
highest_avg = 0
lowest_student = None
lowest_avg = 100

for student in cleaned_students:
    name = student["name"]
    marks = student["marks"]
    
    # Calculate average
    average = sum(marks) / len(marks)
    average_rounded = round(average, 2)
    
    # Get grade
    grade = get_grade(average_rounded)
    
    # Print individual stats
    print(f"{name:<20} | {str(marks):<30} | {average_rounded:<6} | {grade:<6}")
    
    # Track totals
    total_marks_all += average_rounded
    count_students += 1
    
    # Track highest and lowest
    if average_rounded > highest_avg:
        highest_avg = average_rounded
        highest_student = name
    
    if average_rounded < lowest_avg:
        lowest_avg = average_rounded
        lowest_student = name

# Calculate and display overall statistics
print("\n--- Overall Class Statistics ---\n")
class_average = total_marks_all / count_students if count_students > 0 else 0
class_average = round(class_average, 2)

print(f"Total Students:        {count_students}")
print(f"Class Average:         {class_average}")
print(f"Highest Scoring:       {highest_student} ({highest_avg})")
print(f"Lowest Scoring:        {lowest_student} ({lowest_avg})")

# Count pass/fail
pass_count = sum(1 for s in cleaned_students if round(sum(s["marks"])/len(s["marks"]), 2) >= 60)
fail_count = count_students - pass_count

print(f"Students Passed (≥60): {pass_count}")
print(f"Students Failed (<60): {fail_count}")


# ============================================================================
# TASK 3: CLASS PERFORMANCE SUMMARY (7 marks)
# ============================================================================

print("\n" + "="*70)
print("TASK 3: CLASS PERFORMANCE SUMMARY")
print("="*70)

# Generate detailed performance report
print("\n--- Formatted Class Report ---\n")

report_data = []
for student in cleaned_students:
    name = student["name"]
    marks = student["marks"]
    average = round(sum(marks) / len(marks), 2)
    grade = get_grade(average)
    
    # Status based on grade
    if grade == "F":
        status = "Fail"
    else:
        status = "Pass"
    
    report_data.append({
        "name": name,
        "average": average,
        "status": status
    })

# Print formatted table
print(f"{'Name':<20} | {'Average':<10} | {'Status':<10}")
print("-" * 45)

for entry in report_data:
    print(f"{entry['name']:<20} | {entry['average']:<10} | {entry['status']:<10}")

# Print summary after table
print("\n--- Performance Metrics ---")
passed = sum(1 for r in report_data if r['status'] == 'Pass')
failed = sum(1 for r in report_data if r['status'] == 'Fail')
class_topper = max(report_data, key=lambda x: x['average'])
class_average_value = round(sum(r['average'] for r in report_data) / len(report_data), 2)

print(f"Number of students who passed and who failed: Passed={passed}, Failed={failed}")
print(f"Class topper (name = average):                {class_topper['name']} = {class_topper['average']}")
print(f"Class average (average of all five students average): {class_average_value}")


# ============================================================================
# TASK 4: STRING MANIPULATION UTILITY (5 marks)
# ============================================================================

print("\n" + "="*70)
print("TASK 4: STRING MANIPULATION UTILITY")
print("="*70)

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science, web development, and automation.  "

print(f"\nOriginal Essay:\n'{essay}'")

# Step 1: Strip leading and trailing whitespace
clean_essay = essay.strip()
print(f"\n1. After stripping whitespace:\n'{clean_essay}'")

# Step 2: Convert to Title Case
title_essay = clean_essay.title()
print(f"\n2. After converting to Title Case:\n'{title_essay}'")

# Step 3: Count occurrences of 'python' (case-insensitive)
python_count = clean_essay.lower().count("python")
print(f"\n3. Count of 'python' (case-insensitive): {python_count}")

# Step 4: Replace 'python' with 'Python @' and print all occurrences
replaced_essay = clean_essay.lower().replace("python", "Python @")
print(f"\n4. After replacing 'python' with 'Python @':\n'{replaced_essay}'")

# Step 5: Split into sentences and print on new line with numbering
sentences = clean_essay.split(".")
print(f"\n5. Sentences (on separate lines with numbering):")
for i, sentence in enumerate(sentences, 1):
    sentence_clean = sentence.strip()
    if sentence_clean:  # Only print non-empty sentences
        print(f"   {i}. {sentence_clean}.")

# Step 6: Print each sentence on separate line with numbering and period
print(f"\n6. Each sentence on new line (numbered):")
for i, sentence in enumerate(sentences, 1):
    sentence_clean = sentence.strip()
    if sentence_clean:
        print(f"   {i}. {sentence_clean}.")

print("\n" + "="*70)

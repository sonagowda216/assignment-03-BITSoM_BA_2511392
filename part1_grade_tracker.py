"""
Business Analytics Assignment - Part 1: Python Basics & Control Flow
Student Grade Tracker Application

Theme: A command-line Student Grade Tracker that manages student data, computes results, 
and provides a summary report — all using core Python concepts.

This module demonstrates:
- Data parsing and profile cleaning
- String manipulation and validation
- List comprehensions and iterations
- Function design and reusability
- Summary statistics generation
"""
import re

# ============================================================================
# TASK 1: DATA PARSING & PROFILE CLEANING (5 marks)
# ============================================================================

def clean_student_data(raw_students):
    """
    Clean and validate student data from raw format.
    
    Args:
        raw_students (list): List of dictionaries with raw student data
        
    Returns:
        list: List of cleaned student dictionaries
    """
    cleaned_students = []
    
    for student in raw_students:
        # Step 1: Clean and standardize name
        name = student["name"].strip().title()
        
        # Step 2: Convert roll number from string to integer
        roll = int(student["roll"])
        
        # Step 3: Split marks string and convert to list of integers
        marks = [int(m.strip()) for m in student["marks_str"].split(",")]
        
        # Step 4: Validate name (alphabetic characters and spaces only)
        is_valid = all(c.isalpha() or c.isspace() for c in student["name"])
        
        if is_valid:
            validation_status = "✓ Valid name"
        else:
            validation_status = "✗ Invalid name"
        
        print(validation_status)
        
        # Step 5: Print formatted profile card using f-strings
        print("=" * 35)
        print(f"Student : {name}")
        print(f"Roll No : {roll}")
        print(f"Marks   : {marks}")
        print("=" * 35)
        
        # Store cleaned data
        cleaned_students.append({
            "name": name,
            "roll": roll,
            "marks": marks,
            "valid": is_valid
        })
    
    return cleaned_students


def find_student_by_roll(students, roll_number):
    """
    Find a student by roll number.
    
    Args:
        students (list): List of cleaned student dictionaries
        roll_number (int): Roll number to search for
        
    Returns:
        dict: Student dictionary or None if not found
    """
    for student in students:
        if student["roll"] == roll_number:
            return student
    return None


# ============================================================================
# TASK 2: COMPUTE RESULTS & STATISTICS (10 marks)
# ============================================================================

def compute_student_results(students):
    """
    Compute results for all students including marks, grade, and ranking.
    
    Args:
        students (list): List of cleaned student dictionaries
        
    Returns:
        list: Updated students with computed results
    """
    for student in students:
        # Calculate total marks
        student["total"] = sum(student["marks"])
        
        # Calculate average
        student["average"] = student["total"] / len(student["marks"]) if student["marks"] else 0
        
        # Assign grade based on average
        if student["average"] >= 90:
            student["grade"] = "A+"
        elif student["average"] >= 80:
            student["grade"] = "A"
        elif student["average"] >= 70:
            student["grade"] = "B"
        elif student["average"] >= 60:
            student["grade"] = "C"
        elif student["average"] >= 50:
            student["grade"] = "D"
        else:
            student["grade"] = "F"
    
    # Sort by total marks (descending) for ranking
    sorted_students = sorted(students, key=lambda x: x["total"], reverse=True)
    
    # Assign ranks
    for rank, student in enumerate(sorted_students, 1):
        student["rank"] = rank
    
    return students


def compute_class_statistics(students):
    """
    Compute class-level statistics.
    
    Args:
        students (list): List of student dictionaries with computed results
        
    Returns:
        dict: Class statistics
    """
    totals = [s["total"] for s in students]
    averages = [s["average"] for s in students]
    
    stats = {
        "total_students": len(students),
        "class_average": sum(averages) / len(averages) if averages else 0,
        "highest_scorer": max(students, key=lambda x: x["total"]) if students else None,
        "lowest_scorer": min(students, key=lambda x: x["total"]) if students else None,
        "passing_students": sum(1 for s in students if s["average"] >= 50),
        "failing_students": sum(1 for s in students if s["average"] < 50),
    }
    
    return stats


# ============================================================================
# TASK 3: CLASS PERFORMANCE SUMMARY (7 marks)
# ============================================================================


def task3_class_performance(class_data):
    """
    Given class_data as a list of tuples (name, marks_list), compute and print:
    - Average per student (2 decimals)
    - Status: Pass if average >= 60 else Fail
    - Formatted table
    - Number of pass/fail, class topper and class average
    """
    rows = []
    for name, marks in class_data:
        avg = round(sum(marks) / len(marks), 2) if marks else 0.0
        status = "Pass" if avg >= 60 else "Fail"
        rows.append((name, avg, status))

    # Print formatted table
    print("\n" + "=" * 50)
    print("TASK 3 — Class Performance Summary")
    print("=" * 50)
    print(f"{'Name':25} | {'Average':7} | {'Status'}")
    print('-' * 50)
    for name, avg, status in rows:
        print(f"{name:25} | {avg:7.2f} | {status}")

    # Post-table metrics
    pass_count = sum(1 for _, avg, s in rows if s == 'Pass')
    fail_count = sum(1 for _, avg, s in rows if s == 'Fail')
    topper = max(rows, key=lambda r: r[1]) if rows else (None, None, None)
    class_avg = round(sum(r[1] for r in rows) / len(rows), 2) if rows else 0.0

    print("\nSummary:")
    print(f"Passed students : {pass_count}")
    print(f"Failed students : {fail_count}")
    if topper and topper[0]:
        print(f"Class topper    : {topper[0]} -> {topper[1]:.2f}")
    print(f"Class average   : {class_avg:.2f}")

    return {
        'rows': rows,
        'passed': pass_count,
        'failed': fail_count,
        'topper': topper,
        'class_average': class_avg,
    }


# ============================================================================
# TASK 2: MARKS ANALYSIS (loops + conditionals) - integrated for submission
# ============================================================================


def grade_label(mark: int) -> str:
    if 90 <= mark <= 100:
        return "A+"
    if 80 <= mark <= 89:
        return "A"
    if 70 <= mark <= 79:
        return "B"
    if 60 <= mark <= 69:
        return "C"
    if 0 <= mark <= 59:
        return "F"
    return "Invalid"


def print_subjects_with_grades(subjects, marks):
    for subj, mark in zip(subjects, marks):
        print(f"{subj:12} : {mark:3} -> {grade_label(mark)}")


def compute_total_avg_high_low(subjects, marks):
    total = sum(marks)
    avg = round(total / len(marks), 2) if marks else 0.0
    max_idx = marks.index(max(marks)) if marks else None
    min_idx = marks.index(min(marks)) if marks else None

    highest = (subjects[max_idx], marks[max_idx]) if max_idx is not None else (None, None)
    lowest = (subjects[min_idx], marks[min_idx]) if min_idx is not None else (None, None)

    return {
        "total": total,
        "average": avg,
        "highest": highest,
        "lowest": lowest,
    }


def interactive_marks_entry(subjects, marks, simulation=None):
    """
    While-loop based marks entry. If `simulation` provided, it should be a list
    of tuples (subject, mark_or_str) to drive the loop non-interactively.
    """
    new_count = 0
    sim_iter = iter(simulation) if simulation else None

    while True:
        if sim_iter is not None:
            try:
                subj, mark_input = next(sim_iter)
            except StopIteration:
                break
        else:
            subj = input("Enter subject name (or 'done' to finish): ").strip()
            mark_input = None

        if isinstance(subj, str) and subj.lower() == "done":
            break

        if mark_input is None:
            mark_raw = input(f"Enter marks for '{subj}' (0-100): ").strip()
        else:
            mark_raw = str(mark_input)

        try:
            mark = int(mark_raw)
            if not (0 <= mark <= 100):
                print(f"Warning: marks for '{subj}' out of range (0-100). Entry skipped.")
                continue
        except ValueError:
            print(f"Warning: invalid marks input for '{subj}': {mark_raw}. Entry skipped.")
            continue

        subjects.append(subj)
        marks.append(mark)
        new_count += 1

    updated_total = sum(marks)
    updated_avg = round(updated_total / len(marks), 2) if marks else 0.0

    return {
        "subjects": subjects,
        "marks": marks,
        "new_added": new_count,
        "updated_average": updated_avg,
    }


# ============================================================================
# TASK 3: GENERATE SUMMARY REPORT (10 marks)
# ============================================================================

def generate_individual_report(student):
    """
    Generate a formatted individual student report.
    
    Args:
        student (dict): Student dictionary with all data
        
    Returns:
        str: Formatted report
    """
    report = f"""
╔════════════════════════════════════════════════════════════╗
║                    STUDENT REPORT CARD                     ║
╠════════════════════════════════════════════════════════════╣
║ Name        : {student['name']:<42} ║
║ Roll Number : {student['roll']:<42} ║
║ Marks       : {str(student['marks']):<42} ║
║ Total       : {student['total']:<42} ║
║ Average     : {student['average']:<42.2f} ║
║ Grade       : {student['grade']:<42} ║
║ Rank        : {student['rank']:<42} ║
╚════════════════════════════════════════════════════════════╝
"""
    return report


def generate_class_summary_report(students, class_stats):
    """
    Generate a formatted class summary report.
    
    Args:
        students (list): List of student dictionaries
        class_stats (dict): Class statistics
        
    Returns:
        str: Formatted report
    """
    report = f"""
╔════════════════════════════════════════════════════════════╗
║               CLASS SUMMARY REPORT                         ║
╠════════════════════════════════════════════════════════════╣
║ Total Students      : {class_stats['total_students']:<36} ║
║ Class Average       : {class_stats['class_average']:<36.2f} ║
║ Passing Students    : {class_stats['passing_students']:<36} ║
║ Failing Students    : {class_stats['failing_students']:<36} ║
║ Highest Scorer      : {class_stats['highest_scorer']['name']:<36} ║
║ Lowest Scorer       : {class_stats['lowest_scorer']['name']:<36} ║
╚════════════════════════════════════════════════════════════╝

📊 RANK-WISE STUDENT LIST:
"""
    for student in sorted(students, key=lambda x: x["rank"]):
        report += f"\n{student['rank']:2}. {student['name']:25} - Total: {student['total']:3} | Avg: {student['average']:5.2f} | Grade: {student['grade']}"
    
    return report


# ============================================================================
# TASK 4 & 5: CORE LOGIC & SPECIAL OPERATIONS (10 marks)
# ============================================================================

def print_special_operations(students):
    """
    Print special operations on student data.
    - Print name in ALL CAPS and lowercase for specific roll number
    - Demonstrate string case transformations
    """
    # Task requirement: Print name in ALL CAPS and lowercase for roll number 103
    student_103 = find_student_by_roll(students, 103)
    
    if student_103:
        print("\n" + "=" * 50)
        print(f"Special Operations - Roll Number 103:")
        print("=" * 50)
        print(f"Name in ALL CAPS    : {student_103['name'].upper()}")
        print(f"Name in lowercase   : {student_103['name'].lower()}")
        print(f"Name with swapcase  : {student_103['name'].swapcase()}")
        print("=" * 50)


def get_marks_statistics_per_subject(students, num_subjects=None):
    """
    Get statistics for each subject across all students.
    
    Args:
        students (list): List of student dictionaries
        num_subjects (int): Number of subjects (auto-detect if None)
        
    Returns:
        dict: Subject-wise statistics
    """
    if not students:
        return {}
    
    if num_subjects is None:
        num_subjects = len(students[0]["marks"])
    
    subject_stats = {}
    
    for subject_idx in range(num_subjects):
        subject_marks = [s["marks"][subject_idx] for s in students if subject_idx < len(s["marks"])]
        
        if subject_marks:
            subject_stats[f"Subject_{subject_idx + 1}"] = {
                "average": sum(subject_marks) / len(subject_marks),
                "max": max(subject_marks),
                "min": min(subject_marks),
                "total_students": len(subject_marks)
            }
    
    return subject_stats


def task_4_string_utility(clean_essay: str):
    """
    Task 4: Simple string manipulation utility.
    - Splits an essay into sentences and prints them numbered.
    """
    print("\n" + "=" * 50)
    print("TASK 4: STRING MANIPULATION UTILITY")
    print("=" * 50)

    if not isinstance(clean_essay, str) or not clean_essay.strip():
        print("No essay provided or essay is empty.")
        return

    # Split on sentence boundaries (handles ., !, ?), preserve punctuation
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', clean_essay.strip()) if s.strip()]

    print(f"Resulting List: {sentences}\n")

    for i, sentence in enumerate(sentences, 1):
        # Ensure sentence ends with a period if it doesn't already
        if not re.search(r'[.!?]$', sentence):
            sentence = sentence + '.'
        print(f"{i}. {sentence}")



# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Raw student data (as provided in assignment)
    raw_students = [
        {"name": " ayesha SHARMA ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
        {"name": " ROHIT verma ", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
        {"name": " Priya Nair ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
        {"name": " karan MEHTA ", "roll": "104", "marks_str": "40, 55, 38, 62, 58"},
        {"name": " Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
    ]
    
    print("\n" + "=" * 50)
    print("STUDENT GRADE TRACKER - DATA PARSING & CLEANING")
    print("=" * 50 + "\n")
    
    # Step 1: Clean and validate student data
    students = clean_student_data(raw_students)
    
    # Step 2: Compute results
    print("\nComputing results and statistics...\n")
    students = compute_student_results(students)
    class_stats = compute_class_statistics(students)
    
    # Step 3: Print individual reports
    print("\n" + "=" * 50)
    print("INDIVIDUAL STUDENT REPORTS")
    print("=" * 50)
    for student in students:
        print(generate_individual_report(student))
    
    # Step 4: Print class summary
    print("\n" + "=" * 50)
    print("CLASS SUMMARY")
    print("=" * 50)
    print(generate_class_summary_report(students, class_stats))
    
    # Step 5: Special operations
    print_special_operations(students)
    
    # Step 6: Subject-wise statistics
    print("\n" + "=" * 50)
    print("SUBJECT-WISE STATISTICS")
    print("=" * 50)
    subject_stats = get_marks_statistics_per_subject(students)
    for subject, stats in subject_stats.items():
        print(f"\n{subject}:")
        print(f"  Average: {stats['average']:.2f}")
        print(f"  Maximum: {stats['max']}")
        print(f"  Minimum: {stats['min']}")
    
    # ------------------
    # TASK 2: Demonstration (as per assignment screenshot)
    # ------------------
    print("\n" + "=" * 50)
    print("TASK 2 — Marks Analysis Using Loops & Conditionals")
    print("=" * 50)
    student_name = "Ayesha Sharma"
    subjects2 = ["Math", "Physics", "CS", "English", "Chemistry"]
    marks2 = [88, 72, 95, 60, 78]

    print("\nStudent:", student_name)
    print_subjects_with_grades(subjects2, marks2)

    results2 = compute_total_avg_high_low(subjects2, marks2)
    print(f"\nTotal marks     : {results2['total']}")
    print(f"Average marks   : {results2['average']:.2f}")
    print(f"Highest subject : {results2['highest'][0]} -> {results2['highest'][1]}")
    print(f"Lowest subject  : {results2['lowest'][0]} -> {results2['lowest'][1]}")

    simulation = [
        ("Biology", 82),
        ("Art", "abc"),     # invalid -> should be skipped with warning
        ("Geography", 74),
        ("done", None),
    ]
    after = interactive_marks_entry(subjects2[:], marks2[:], simulation=simulation)
    print(f"\nNew subjects added: {after['new_added']}")
    print(f"Updated average (original + new): {after['updated_average']:.2f}")

    print("\n" + "=" * 50)
    print("EXECUTION COMPLETED SUCCESSFULLY")
    print("=" * 50 + "\n")

    # ------------------
    # Task 4: Example usage
    # ------------------
    example_essay = (
        "This is the first sentence. Here is the second sentence! "
        "Is this the third sentence? Yes it is"
    )
    task_4_string_utility(example_essay)

"""
Task 2 — Marks Analysis Using Loops & Conditionals

This script implements the Task 2 requirements from Part 1:
1) Use a for-loop to print each subject with marks and grade label.
2) Calculate total marks, average (2 decimals), highest and lowest scoring subject.
3) Use a while-loop to allow adding new subjects interactively (or via a simulation list),
   validate inputs, and print updated counts and averages.

The module provides functions suitable for unit testing and a demo runner.
"""
from typing import List, Tuple, Dict, Optional


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


def print_subjects_with_grades(subjects: List[str], marks: List[int]) -> None:
    for subj, mark in zip(subjects, marks):
        print(f"{subj:12} : {mark:3} -> {grade_label(mark)}")


def compute_total_avg_high_low(subjects: List[str], marks: List[int]) -> Dict[str, object]:
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


def interactive_marks_entry(subjects: List[str], marks: List[int], simulation: Optional[List[Tuple[str, object]]] = None) -> Dict[str, object]:
    """
    Launch a while-loop to accept new subject entries.

    If `simulation` is provided it should be a list of tuples (subject, mark_or_str),
    where mark_or_str may be an int or the string 'done' to stop.

    Returns a dict with updated lists, count of new subjects, and updated average.
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

        # Validate mark
        try:
            mark = int(mark_raw)
            if not (0 <= mark <= 100):
                print(f"Warning: marks for '{subj}' out of range (0-100). Entry skipped.")
                continue
        except ValueError:
            print(f"Warning: invalid marks input for '{subj}': {mark_raw}. Entry skipped.")
            continue

        # Accept the new subject
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


def demo():
    student_name = "Ayesha Sharma"
    subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
    marks = [88, 72, 95, 60, 78]

    print("\nTask 2 — Marks Analysis Using Loops & Conditionals")
    print("Student:", student_name)
    print("\n1) Subjects with grades:")
    print_subjects_with_grades(subjects, marks)

    print("\n2) Calculations:")
    results = compute_total_avg_high_low(subjects, marks)
    print(f"Total marks     : {results['total']}")
    print(f"Average marks   : {results['average']:.2f}")
    print(f"Highest subject : {results['highest'][0]} -> {results['highest'][1]}")
    print(f"Lowest subject  : {results['lowest'][0]} -> {results['lowest'][1]}")

    print("\n3) Simulated marks-entry using while-loop (adds two valid and one invalid entry):")
    simulation = [
        ("Biology", 82),
        ("Art", "abc"),     # invalid -> should be skipped with warning
        ("Geography", 74),
        ("done", None),
    ]

    after = interactive_marks_entry(subjects[:], marks[:], simulation=simulation)
    print(f"\nNew subjects added: {after['new_added']}")
    print(f"Updated average (original + new): {after['updated_average']:.2f}")


if __name__ == "__main__":
    demo()

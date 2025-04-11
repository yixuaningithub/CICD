import subprocess
from pathlib import Path
import shutil
import csv

DICTIONARY_FILE = "dictionary.txt"
CSV_OUTPUT = "grading_results.csv"

def test_student(student_path: Path):
    shutil.copy(DICTIONARY_FILE, student_path / "dictionary.txt")

    input_data = "\n".join([
        "f y c l",
        "i o m g",
        "o r i l",
        "h j h u"
    ]) + "\n"

    result = subprocess.run(
        ["python3", "boggle.py"],
        input=input_data,
        capture_output=True,
        text=True,
        cwd=student_path
    )

    passed = "found" in result.stdout.lower() and "words in total" in result.stdout.lower()
    return {
        "student": student_path.name,
        "status": "PASS" if passed else "FAIL"
    }

def main():
    student_dirs = Path("students").glob("*")
    results = []

    for student in student_dirs:
        if (student / "boggle.py").exists():
            result = test_student(student)
            results.append(result)

    # Write to CSV
    with open(CSV_OUTPUT, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["student", "status"])
        writer.writeheader()
        writer.writerows(results)

    print("✅ Results written to", CSV_OUTPUT)

if __name__ == "__main__":
    main()

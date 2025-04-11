import subprocess
from pathlib import Path
import shutil

DICTIONARY_FILE = "dictionary.txt"


def test_student(student_path: Path):
    # Copy the shared dictionary.txt to the student folder (temporary)
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

    print(f"\n== Testing {student_path.name} ==")
    if "found" in result.stdout.lower() and "words in total" in result.stdout.lower():
        print("Test passed")
    else:
        print("Test failed")
        print(result.stdout)
        print(result.stderr)


def main():
    student_dirs = Path("students").glob("*")
    for student in student_dirs:
        if (student / "boggle.py").exists():
            test_student(student)


if __name__ == "__main__":
    main()

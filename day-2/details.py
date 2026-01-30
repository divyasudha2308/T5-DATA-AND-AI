import os

def format_name(name):
    return name.strip().title()

def view_courses(courses):
    print("\nAvailable Courses:")
    for idx, course in enumerate(courses, 1):
        print(f"{idx}. {course}")

def select_courses(courses, *selected_numbers):
    selected_courses = []
    for num in selected_numbers:
        if 1 <= num <= len(courses):
            selected_courses.append(courses[num-1])
    return selected_courses

def profile_summary(**kwargs):
    summary = ""
    for key, value in kwargs.items():
        summary += f"{key.replace('_',' ').title()}: {value}\n"
    return summary

def save_summary_to_file(student_name, summary_text, folder="registrations"):
    if not os.path.exists(folder):
        os.makedirs(folder)  # create folder if it doesn't exist
    filename = f"{folder}/{student_name.replace(' ','_')}_registration.txt"
    with open(filename, "w") as f:
        f.write(summary_text)
    print(f"\nSummary saved to {filename}")

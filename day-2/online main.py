from details import format_name, view_courses, select_courses, profile_summary, save_summary_to_file

available_courses = ["pharamcy", "psychology", "arts", "honours", "Computers"]

name = format_name(input("Enter student name: "))
age = input("Enter student age: ")

all_registered_courses = []

while True:
    view_courses(available_courses)

    course_numbers = input("Enter course numbers to register (comma separated): ")
    selected_numbers = [int(num.strip()) for num in course_numbers.split(",")]

    new_courses = select_courses(available_courses, *selected_numbers)
    all_registered_courses.extend(new_courses)

    more = input("Do you want to register more courses? (yes/no): ").strip().lower()
    if more != "yes":
        break

student_profile = profile_summary(
    name=name,
    age=age,
    registered_courses=", ".join(all_registered_courses),
    total_courses=len(all_registered_courses)
)

print("\n--- Student Registration Summary ---")
print(student_profile)

save_summary_to_file(name, student_profile)

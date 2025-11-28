import datetime

# Initialize an empty schedule dictionary
schedule = {}

# Valid days constant (module-level)
VALID_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def add_class():
    course_name = input("Enter course name: ")

    # Validate day input
    while True:
        day_input = input("Enter day of the week (Monday–Sunday): ").strip()
        # Normalize input (handles 'monday', 'MONDAY', etc.)
        day = day_input.capitalize()
        if day in VALID_DAYS:
            break
        else:
            print("Invalid day. Please enter a valid day (Monday–Sunday).")

    # Validate time input
    while True:
        time_str = input("Enter class time (HH:MM, 24-hour format): ").strip()
        try:
            datetime.datetime.strptime(time_str, "%H:%M")  # validate format
            break
        except ValueError:
            print("Invalid time format. Use HH:MM (e.g., 09:30 or 14:00).")

    if day not in schedule:
        schedule[day] = []
    schedule[day].append({'name': course_name, 'time': time_str})
    print(f"Added {course_name} on {day} at {time_str}.")

def view_schedule():
    print("\nYour Class Schedule:")
    for day in VALID_DAYS:
        print(f"\n{day}:")
        if day in schedule and schedule[day]:
            # Sort by time for nicer display
            for cls in sorted(schedule[day], key=lambda x: x['time']):
                print(f" {cls['time']} - {cls['name']}")
        else:
            print(" No classes scheduled.")

def get_reminders():
    now = datetime.datetime.now()
    current_day = now.strftime("%A")
    current_time = now.strftime("%H:%M")
    print(f"\nCurrent time: {current_time} on {current_day}")

    if current_day in schedule and schedule[current_day]:

        current_time_obj = datetime.datetime.strptime(current_time, "%H:%M").time()
        upcoming_classes = []
        for cls in schedule[current_day]:
            try:
                class_time_obj = datetime.datetime.strptime(cls['time'], "%H:%M").time()
            except ValueError:

                continue
            if class_time_obj >= current_time_obj:
                upcoming_classes.append(cls)

        if upcoming_classes:
            print("Upcoming classes for today:")
            for cls in sorted(upcoming_classes, key=lambda x: x['time']):
                print(f" {cls['time']} - {cls['name']}")
        else:
            print("No more classes today.")
    else:
        print("No classes scheduled for today.")

def main():
    while True:
        print("\nClass Schedule Reminder System")
        print("1. Add a class")
        print("2. View schedule")
        print("3. Get today's reminders")
        print("4. Exit")
        choice = input("Select an option (1-4): ").strip()
        if choice == '1':
            add_class()
        elif choice == '2':
            view_schedule()
        elif choice == '3':
            get_reminders()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
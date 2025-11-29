import datetime

schedule = {}
schedule['Monday'] = []

schedule['Monday'].append({'name': 'a', 'time': '10:22'})

week_of_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def add_course():
    course_name = input("Enter the name of the course: ")
   
    while True:
        course_date = input("Enter the day of week of the course (Monday - Sunday): ")
        course_date = course_date.capitalize()
        if course_date in week_of_day:
            break
        else:
            print("Invalid Week of Day")
    
    while True:
        course_time = input("Enter the time of course (HH:MM, 24-hour format): ").strip()
        try:
            datetime.datetime.strptime(course_time, "%H:%M")
            break
        except ValueError:
            print("Invalid Time")
    
    if course_date not in schedule:
        schedule[course_date] = []
    
    
    for course in schedule[course_date]:
        if course['name'] == course_name and course['time'] == course_time:
            print("already exists")
            return
    
    # Add course if not duplicate
    schedule[course_date].append({'name': course_name, 'time': course_time})
    print(f"Added {course_name} on {course_date} at {course_time}.")

def view_schedule():
    print("\nSchedule:")
    for d in week_of_day:
        print(d)
        if d in schedule and schedule[d]:
            for course in schedule[d]:
                print(f"  {course['name']} : {course['time']}")
def get_reminders():
    nowtime = datetime.datetime.now()
    current_day = 'Monday'
    current_time = '10:22'
    print(f"\nCurrent time: {current_time} on {current_day}")
    print("current course: ")
    if current_day in schedule and schedule[current_day]:
        for course in schedule[current_day]:
            if  course['time'] == current_time :
                print(f"  {course['name']} : {course['time']}")
                return
    print("upcoming Course in 30Mins:")
    if current_day in schedule and schedule[current_day]:
        for course in schedule[current_day]:
            if  course['time'] == current_time+30 :
                print(f"  {course['name']} : {course['time']}")
                return
        
    
get_reminders()





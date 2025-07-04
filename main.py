import time
from datetime import datetime

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"Focus session started for {minutes} minutes.")

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time.sleep(1)
        seconds -= 1

    print("Time's up! Great job!")

    # Session Logging
    with open("session_log.txt", "a") as log_file:
        log_file.write(f"Session completed: {minutes} minutes at {datetime.now()}\n")
<<<<<<< HEAD

def show_today_summary():
    today = datetime.now().date()
    session_count = 0
    total_minutes = 0

=======
                        
if __name__ == "__main__":

    # User Input
>>>>>>> 38b83dc51da028ba996c3f446691e1d96c38468a
    try:
        with open("session_log.txt", "r") as log_file:
            for line in log_file:
                if "Session completed" in line:
                    parts = line.strip().split(" at ")
                    minutes_part = parts[0].split(":")[1].strip().split()[0]
                    time_part = parts[1]

                    try:
                        session_time = datetime.strptime(time_part.strip(), "%Y-%m-%d %H:%M:%S.%f")
                    except ValueError:
                        continue

                    if session_time.date() == today:
                        session_count += 1
                        total_minutes += float(minutes_part)

        print(f"\n--- Daily Summary ---")
        print(f"Sessions today: {session_count}")
        print(f"Total focus minutes: {round(total_minutes, 2)}")
        print("---------------------\n")

    except FileNotFoundError:
        print("No session log found.")

if __name__ == "__main__":
    try:
        minutes = float(input("Enter focus session length in minutes: "))
        focus_timer(minutes)
        show_today_summary()
    except ValueError:
<<<<<<< HEAD
        print("Please enter a valid number.")
=======
        print("Please enter a valid number. ")
>>>>>>> 38b83dc51da028ba996c3f446691e1d96c38468a

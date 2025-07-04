import time
from datetime import datetime
from collections import defaultdict

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

def show_today_summary():
    today = datetime.now().date()
    session_count = 0
    total_minutes = 0

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

def visualize_sessions_ascii():
    try:
        daily_totals = defaultdict(float)
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

                    date_str = session_time.strftime("%Y-%m-%d")
                    daily_totals[date_str] += float(minutes_part)

        print("\nDaily Focus Summary:")
        print("---------------------")
        for date in sorted(daily_totals.keys()):
            minutes = daily_totals[date]
            bar = "█" * int(minutes / 2)  # each block = 2 minutes
            print(f"{date} | {bar:<25} {int(minutes)} mins")

    except FileNotFoundError:
        print("No session log found.")

if __name__ == "__main__":
    try:
        minutes = float(input("Enter focus session length in minutes: "))
        focus_timer(minutes)
        show_today_summary()
        visualize_sessions_ascii()

    except ValueError:
        print("Please enter a valid number.")

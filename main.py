import time
from datetime import datetime
from collections import defaultdict
from emotional_tracker import log_emotion
import msvcrt

def focus_timer(minutes):
    seconds = int(minutes * 60)
    print(f"Focus session started for {minutes} minutes.")
    print("Press [p] to pause, [r] to resume, [q] to quit.\n")
    
    paused = False

    while seconds > 0:
        if not paused:
            mins, secs = divmod(seconds, 60)
            print(f"\rTime Remaining: {mins:02d}:{secs:02d}", end="")
            time.sleep(1)
            seconds -= 1
        else:
            print("\r[Paused] Press [r] to resume or [q] to quit.", end="")
            time.sleep(1)

        # Check for keypress
        if msvcrt.kbhit():
            key = msvcrt.getwch().lower()
            if key == 'p':
                paused = True
                print("\nPaused.")
            elif key == 'r' and paused:
                paused = False
                print("\nResumed.")
            elif key == 'q':
                print("\n[Session cancelled by user.]")
                return

    print("\nTime's up! Great job!")

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
        
        print("\nReflect on that session:")
        log_emotion()
        
    except ValueError:
        print("Please enter a valid number.")

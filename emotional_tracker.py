from collections import Counter, defaultdict
from datetime import datetime, timedelta

import os

def log_emotion():
    print("\n--- Emotion Logger ---" )
    
    emotion =  input("Emotion (e.g., happy, anxious, focused): ").strip().capitalize()
    if not emotion:
        print("Emotion cannot be empty.")
        return
    
    try:
        intensity = int(input("Intensity (1 - 10): "))
        if intensity < 1 or intensity > 10: 
            raise ValueError
    except ValueError:
        print("Please enter a valid number between 1 and 10. ")
        return

    note = input("Optional note: ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    entry = f"{timestamp} | {emotion} | {intensity} | {note}\n"
    
    try:
        with open("emotion_log.txt", "a") as file:
            file.write(entry)
        print("✌  Emotion Logged. ")
    
    except Exception as e:
        print("Error saving entry:", e)    


def emotion_summary():
    try:
        with open("emotion_log.txt", "r") as file:
            emotions = []
            
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) >= 2:
                    emotion = parts[1].strip().capitalize()
                    emotions.append(emotion)
                    
            if emotions: 
                counts = Counter(emotions)
                total = sum(counts.values())
                
                print('\n--- Emotion Summary ---')
                for emotion, count in counts.most_common():
                    print(f"{emotion:<12} : {count} times")
                print(f"Total Entries   : {total}")
                print("------------------------\n")
            else:
                print("No emotion data found.")
                
    except FileNotFoundError:
        print("No emotion log file found.")
        

def summary_today():
    try:
        with open("emotion_log.txt", "r") as file:
            emotions = []
            today = datetime.now().date()

            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) >= 2:
                    timestamp_str = parts[0].strip()
                    emotion = parts[1].strip().capitalize()

                    try:
                        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
                        if timestamp.date() == today:
                            emotions.append(emotion)
                    except ValueError:
                        continue

            if emotions:
                counts = Counter(emotions)
                total = sum(counts.values())

                print("\n--- Today's Emotion Summary ---")
                for emotion, count in counts.most_common():
                    print(f"{emotion:<12} : {count} times")
                print(f"Total Entries   : {total}")
                print("-------------------------------\n")
            else:
                print("No emotion data for today.")

    except FileNotFoundError:
        print("No emotion log found.")
                
def summary_this_week():
    try:
        with open("emotion_log.txt", "r") as file:
            emotions = []
            today = datetime.now().date()
            one_week_ago = today - timedelta(days=7)

            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) >= 2:
                    timestamp_str = parts[0].strip()
                    emotion = parts[1].strip().capitalize()

                    try:
                        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
                        if one_week_ago <= timestamp.date() <= today:
                            emotions.append(emotion)
                    except ValueError:
                        continue

            if emotions:
                counts = Counter(emotions)
                total = sum(counts.values())

                print("\n--- This Week's Emotion Summary ---")
                for emotion, count in counts.most_common():
                    print(f"{emotion:<12} : {count} times")
                print(f"Total Entries   : {total}")
                print("-----------------------------------\n")
            else:
                print("No emotion data from the past 7 days.")

    except FileNotFoundError:
        print("No emotion log found.")
        
def emotion_weekly_timeline():
    try:
        daily_emotions = defaultdict(list)
        today = datetime.now().date()
        one_week_ago = today - timedelta(days=6)  # last 7 days including today

        with open("emotion_log.txt", "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) >= 2:
                    timestamp_str = parts[0].strip()
                    emotion = parts[1].strip().capitalize()

                    try:
                        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
                        if one_week_ago <= timestamp.date() <= today:
                            date_key = timestamp.date().strftime("%a %d")
                            daily_emotions[date_key].append(emotion)
                    except ValueError:
                        continue

        if daily_emotions:
            print("\n--- Weekly Emotion Timeline ---")
            for date in sorted(daily_emotions.keys()):
                counts = Counter(daily_emotions[date])
                bar = ""
                for emotion, count in counts.items():
                    symbol = emotion[0].upper()  # first letter as marker
                    bar += f"{symbol * count} "
                print(f"{date:<10} | {bar}")
            print("--------------------------------\n")
        else:
            print("No emotion data for the past 7 days.")

    except FileNotFoundError:
        print("No emotion log found.")
        
def emotion_ascii_graph():
    try:
        with open("emotion_log.txt", "r") as file:
            emotions = []
            today = datetime.now().date()
            one_week_ago = today - timedelta(days=7)

            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) >= 2:
                    timestamp_str = parts[0].strip()
                    emotion = parts[1].strip().capitalize()

                    try:
                        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
                        if one_week_ago <= timestamp.date() <= today:
                            emotions.append(emotion)
                    except ValueError:
                        continue

            if emotions:
                counts = Counter(emotions)

                print("\n--- Emotion Frequency (This Week) ---")
                for emotion, count in counts.most_common():
                    bar = "█" * count
                    print(f"{emotion:<12} | {bar} {count}")
                print("-------------------------------------\n")
            else:
                print("No emotion data from the past 7 days.")

    except FileNotFoundError:
        print("No emotion log found.")

                   
        
def menu():
    while True:
        print("\n--- Emotion Tracker Menu ---")
        print("1. Log a new emotion")
        print("2. Show full emotion summary")
        print("3. Show today’s emotion summary")
        print("4. Show this week’s emotion summary")
        print("5. Show Weekly Emotion Timeline")
        print("6. Show ASCII Emotion Graph (This Week)")
        print("7. Exit")
        choice = input("Choose an option (1–7): ").strip()

        if choice == "1":
            log_emotion()
        elif choice == "2":
            emotion_summary()
        elif choice == "3":
            summary_today()
        elif choice == "4":
            summary_this_week()
        elif choice == "5":
            emotion_weekly_timeline()
        elif choice == "6":
            emotion_ascii_graph()
        elif choice == "7":
            print("Exiting. Stay aware ✌")
            break
        else:
            print("Invalid choice. Try again.")
            
if __name__ == "__main__":
    menu()

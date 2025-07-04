import time
from datetime import datetime

def focus_timer(minutes):
    seconds = minutes * 60
    print (f"Focus session started for {minutes} minutes.")
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time.sleep(1)
        seconds -= 1
    
    print("Time's up! Great job!")
      
   #Session Logging
   
    with open("session_log.txt", "a") as log_file:
        log_file.write(f"Session completed: {minutes} minutes at {datetime.now()}\n")
                        
if __name__ == "__main__":
    
    try:
        minutes = int(input("Enter focus session length in minutes: "))
        focus_timer(minutes)
        
    except ValueError:
        print("Please enter a valid number. ")
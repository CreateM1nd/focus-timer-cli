import time

def focus_timer(minutes):
    seconds = minutes * 60
    print (f"Focus session started for {minutes} minutes.")
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time.sleep(1)
        seconds -= 1
    
    print("Time's up! Great job!")
    
if __name__ == "__main__":
    focus_timer(25) # Default 25 minute session
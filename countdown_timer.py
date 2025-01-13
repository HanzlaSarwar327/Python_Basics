# Countdown Timer with Beep Sound

import time
import os  # For making a beep sound

def beep():
    # Cross-platform way to produce a beep sound
    try:
        # Windows
        if os.name == 'nt':
            import winsound
            winsound.Beep(1000, 500)  # Frequency: 1000 Hz, Duration: 500 ms
        else:
            # macOS/Linux
            print('\a', end='', flush=True)
    except Exception as e:
        print(f"Error: Unable to produce a beep sound. {e}")

def countdown_timer():
    try:
        seconds = int(input("Enter the time in seconds for the countdown: "))
        print(f"Countdown started for {seconds} seconds!")
        
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(timer, end="\r")  # Overwrites the same line in the terminal
            time.sleep(1)
            seconds -= 1
        
        print("Time's up! 🚨")
        beep()  # Play the beep sound when the timer ends
    except ValueError:
        print("Error: Please enter a valid number of seconds.")

if __name__ == "__main__":
    countdown_timer()

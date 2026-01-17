import time
from . import listener
from . import actions
from .utils import speak

def main():
    print("Friday Assistant Started")
    
    while True:
        # 1. Wait for "Friday"
        if not listener.wait_for_wake_word():
            break # Exit if KeyboardInterrupt
            
        speak("Yes? Waiting for clap.")
        
        # 2. Wait for Clap
        if listener.wait_for_clap():
            # 3. Perform Actions
            actions.perform_actions()
            
            # Optional: Wait a bit before listening again to avoid immediate re-trigger
            time.sleep(5) 
            
            print("Resetting... Waiting for 'Friday' again.")

if __name__ == "__main__":
    main()

import webbrowser
from .utils import speak

def perform_actions():
    """Opens websites and plays music."""
    speak("Clap detected. Performing actions.")
    
    print("Opening Google...")
    webbrowser.open("https://www.google.com")
    
    print("Opening YouTube...")
    webbrowser.open("https://www.youtube.com")
    
    print("Playing music...")
    # Placeholder: Song "Rick Astley - Never Gonna Give You Up"
    music_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
    webbrowser.open(music_url)

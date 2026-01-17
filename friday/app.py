import speech_recognition as sr
# import pyttsx3 # Removed as per user request
import webbrowser
import pyaudio
import numpy as np
import struct
import time

# Configuration
CLAP_THRESHOLD = 200 # Adjust this value based on mic sensitivity (1000-5000 usually)
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Initialize engines
recognizer = sr.Recognizer()
# engine = pyttsx3.init() # Removed

def speak(text):
    """Prints feedback to the user (formerly spoke it)."""
    print(f"[Friday]: {text}")
    # engine.say(text)
    # engine.runAndWait()

def wait_for_wake_word():
    """Listens continuously for the wake word 'Friday'."""
    print("Waiting for wake word 'Friday'...")
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                # Listen for a short phrase
                audio = recognizer.listen(source, phrase_time_limit=3)
            
            try:
                text = recognizer.recognize_google(audio).lower()
                if "friday" in text:
                    print("Wake word detected!")
                    return True
            except sr.UnknownValueError:
                pass # No speech recognized
            except sr.RequestError:
                print("Network error (Speech Recognition)")
                time.sleep(1)
        except KeyboardInterrupt:
            return False
        except Exception as e:
            # print(f"Error in wake word listener: {e}") 
            continue

def wait_for_clap():
    """Listens for a loud sound (clap) exceeding the threshold."""
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for CLAPS...")
    speak("Ready for clap.")
    
    try:
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            # Convert audio data to integers
            audio_data = np.frombuffer(data, dtype=np.int16)
            # Calculate RMS amplitude
            rms = np.sqrt(np.mean(audio_data**2))
            
            if rms > CLAP_THRESHOLD:
                print(f"Clap detected! (RMS: {rms:.2f})")
                return True
                
    except KeyboardInterrupt:
        return False
    except Exception as e:
        print(f"Error in clap listener: {e}")
        return False
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

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

def main():
    print("Friday Assistant Started")
    
    while True:
        # 1. Wait for "Friday"
        if not wait_for_wake_word():
            break # Exit if KeyboardInterrupt
            
        speak("Yes? Waiting for clap.")
        
        # 2. Wait for Clap
        if wait_for_clap():
            # 3. Perform Actions
            perform_actions()
            
            # Optional: Wait a bit before listening again to avoid immediate re-trigger
            time.sleep(5) 
            
            print("Resetting... Waiting for 'Friday' again.")

if __name__ == "__main__":
    main()

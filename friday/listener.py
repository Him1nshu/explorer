import speech_recognition as sr
import pyaudio
import numpy as np
import time
from . import config
from .utils import speak

# Initialize recognizer
recognizer = sr.Recognizer()

def wait_for_wake_word():
    """Listens continuously for the wake word."""
    print(f"Waiting for wake word '{config.WAKE_WORD}'...")
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                # Listen for a short phrase
                audio = recognizer.listen(source, phrase_time_limit=3)
            
            try:
                text = recognizer.recognize_google(audio).lower()
                if config.WAKE_WORD in text:
                    print("Wake word detected!")
                    return True
            except sr.UnknownValueError:
                pass # No speech recognized
            except sr.RequestError:
                print("Network error (Speech Recognition)")
                time.sleep(1)
        except KeyboardInterrupt:
            return False
        except Exception:
            continue

def wait_for_clap():
    """Listens for a loud sound (clap) exceeding the threshold."""
    p = pyaudio.PyAudio()
    stream = p.open(format=config.FORMAT,
                    channels=config.CHANNELS,
                    rate=config.RATE,
                    input=True,
                    frames_per_buffer=config.CHUNK)

    print("Listening for CLAPS...")
    speak("Ready for clap.")
    
    try:
        while True:
            data = stream.read(config.CHUNK, exception_on_overflow=False)
            # Convert audio data to integers
            audio_data = np.frombuffer(data, dtype=np.int16)
            # Calculate RMS amplitude
            rms = np.sqrt(np.mean(audio_data**2))
            
            if rms > config.CLAP_THRESHOLD:
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

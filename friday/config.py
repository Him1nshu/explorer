import pyaudio

# Mic Sensitivity
# Adjust this value based on mic sensitivity (1000-5000 usually)
CLAP_THRESHOLD = 200 

# Audio Format
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Wake Word
WAKE_WORD = "friday"

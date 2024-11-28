import soundfile as sf
import sounddevice as sd

def load_audio(file_path):
    audio_data, sr = sf.read(file_path)
    return audio_data, sr

def save_audio(file_path, audio_data, sr):
    sf.write(file_path, audio_data, sr)

def record_audio(duration, sr=44100):
    print("Recording...")
    audio_data = sd.rec(int(duration * sr), samplerate=sr, channels=1, dtype='float32')
    sd.wait()
    print("Recording complete.")
    return audio_data.flatten(), sr

def play_audio(audio_data, sr):
    print("Playing audio...")
    sd.play(audio_data, samplerate=sr)
    sd.wait()

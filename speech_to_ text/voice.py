import whisper

# Step 1: Load the Whisper model
# Choose model size: tiny, base, small, medium, large
print("Loading Whisper model...")
model = whisper.load_model("base")

# Step 2: Path to the .wav file
audio_file = "harvard.wav"  # Replace with the path to your .wav file

# Step 3: Transcribe the audio file
print(f"Transcribing file: {audio_file}...")
result = model.transcribe(audio_file)

# Step 4: Output the transcription
print("\nTranscription:")
print(result["text"])

# Optional: Print detailed segments with timestamps
print("\nDetailed Transcription with Timestamps:")
for segment in result['segments']:
    print(f"[{segment['start']:.2f} - {segment['end']:.2f}]: {segment['text']}")

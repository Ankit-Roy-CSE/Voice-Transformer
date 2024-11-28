import argparse
import os
from effects import apply_effect
from utils import load_audio, save_audio, record_audio, play_audio

def main():
    parser = argparse.ArgumentParser(description="Voice Changer Application")
    parser.add_argument("--file", type=str, help="Path to the input audio file")
    parser.add_argument("--effect", type=str, required=True, choices=["robot", "pitch_up", "pitch_down", "reverb"],
                        help="Effect to apply to the audio")
    parser.add_argument("--realtime", action="store_true", help="Enable real-time voice processing")
    args = parser.parse_args()

    if args.realtime:
        print("Recording real-time audio. Speak into your microphone.")
        audio_data, sr = record_audio(duration=5)
        print("Applying effect...")
        transformed_audio = apply_effect(audio_data, sr, args.effect)
        print("Playing transformed audio...")
        play_audio(transformed_audio, sr)
    elif args.file:
        if not os.path.exists(args.file):
            print(f"File not found: {args.file}")
            return
        print(f"Loading audio file: {args.file}")
        audio_data, sr = load_audio(args.file)
        print("Applying effect...")
        transformed_audio = apply_effect(audio_data, sr, args.effect)
        output_path = os.path.join("output", f"transformed_{os.path.basename(args.file)}")
        save_audio(output_path, transformed_audio, sr)
        print(f"Transformed audio saved at: {output_path}")
    else:
        print("Please provide either a file path or enable real-time mode using --realtime.")

if __name__ == "__main__":
    main()

import argparse
import os
from TTS.TTS.api import TTS
from pathlib import Path

def create_tts_cli():
    parser = argparse.ArgumentParser(description='Text to Speech CLI Tool')
    parser.add_argument('--text', type=str, help='Text to convert to speech')
    parser.add_argument('--input-file', type=str, help='Text file to convert to speech')
    parser.add_argument('--output', type=str, default='output.wav', help='Output audio file path')
    parser.add_argument('--speaker', type=str, help='Path to speaker voice sample')
    # parser.add_argument('--language', type=str, help='Language code (default: en)')
    return parser

def process_tts(text, output_path, speaker_path=None, language='en'):
    try:
        tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")
        print(f"Converting text to speech...")
        tts.tts_to_file(
            text=text,
            file_path=output_path,
            speaker_wav=speaker_path if speaker_path else None,
            split_sentences=True
        )
        print(f"Audio saved to: {output_path}")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return False
    return True

def main():
    parser = create_tts_cli()
    args = parser.parse_args()

    if not args.text and not args.input_file:
        parser.error("Either --text or --input-file must be provided")

    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    if args.input_file:
        try:
            with open(args.input_file, 'r') as f:
                text = f.read()
        except Exception as e:
            print(f"Error reading input file: {str(e)}")
            return
    else:
        text = args.text

    success = process_tts(
        text=text,
        output_path=args.output,
        speaker_path=args.speaker,
        # language=args.language
    )

    if not success:
        print("TTS conversion failed")
        return

if __name__ == "__main__":
    main()
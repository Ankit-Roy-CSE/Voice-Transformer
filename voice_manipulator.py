import librosa
import librosa.display
import soundfile as sf
import click
import os
from pathlib import Path

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--effect', type=click.Choice(['speed', 'pitch', 'reverse', 'echo']), required=True, help="Choose the effect.")
@click.option('--value', default=1.0, help="Effect parameter: e.g., speed factor, pitch shift steps, etc.")
def manipulate_audio(input_file, output_file, effect, value):
    """
    CLI Tool to manipulate audio files with effects like speed change, pitch shift, reverse, or echo.
    """
    input_path = str(input_path) if isinstance(input_path, Path) else input_path
    output_path = str(output_path) if isinstance(output_path, Path) else output_path
    try:
        # Load audio file
        audio, sr = librosa.load(input_file, sr=None)
        
        if effect == 'speed':
            audio = librosa.effects.time_stretch(audio, rate=value)
        elif effect == 'pitch':
            audio = librosa.effects.pitch_shift(audio, sr=sr, n_steps=value)
        elif effect == 'reverse':
            audio = audio[::-1]
        elif effect == 'echo':
            echo = librosa.util.fix_length(audio,size= (len(audio) + int(sr * value)))
            echo[-len(audio):] += audio * 0.6
            audio = echo

        # Save the processed audio
        sf.write(output_file, audio, sr)
        click.echo(f"Audio file saved with '{effect}' effect at: {output_file}")

    except Exception as e:
        click.echo(f"Error: {str(e)}")

if __name__ == "__main__":
    manipulate_audio()

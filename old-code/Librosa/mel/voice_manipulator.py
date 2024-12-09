import librosa
import librosa.display
import soundfile as sf
import click
import numpy as np
import matplotlib.pyplot as plt

def visualize_mel_spectrogram(mel_spectrogram, sr):
    
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(mel_spectrogram_db, sr=sr, x_axis='time', y_axis='mel', fmax=8000, cmap='viridis')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel Spectrogram')
    plt.tight_layout()
    plt.show()

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--value', default=1.0, help="Magnitude")
def manipulate_audio(input_file, output_file, value):
    
    try:
        
        audio, sr = librosa.load(input_file, sr=None)


        mel_spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=128, fmax=8000)
        visualize_mel_spectrogram(mel_spectrogram, sr)
        mel_spectrogram *= value
            
        visualize_mel_spectrogram(mel_spectrogram, sr)

        audio = librosa.feature.inverse.mel_to_audio(mel_spectrogram, sr=sr)
        sf.write(output_file, audio, sr)
        click.echo(f"Audio file saved with at: {output_file}")

    except Exception as e:
        click.echo(f"Error: {str(e)}")

if __name__ == "__main__":
    manipulate_audio()

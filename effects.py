import numpy as np
import librosa
import librosa.effects

def apply_effect(audio_data, sr, effect):
    if effect == "robot":
        return robot_effect(audio_data)
    elif effect == "pitch_up":
        return pitch_shift(audio_data, sr, n_steps=4)
    elif effect == "pitch_down":
        return pitch_shift(audio_data, sr, n_steps=-4)
    elif effect == "reverb":
        return reverb_effect(audio_data)
    else:
        raise ValueError(f"Unknown effect: {effect}")

def robot_effect(audio_data):
    return np.sign(audio_data)

def pitch_shift(audio_data, sr, n_steps):
    return librosa.effects.pitch_shift(audio_data, sr, n_steps=n_steps)

def reverb_effect(audio_data):
    reverb_kernel = np.hanning(1024)  # Simplistic reverb kernel
    return np.convolve(audio_data, reverb_kernel, mode='same')

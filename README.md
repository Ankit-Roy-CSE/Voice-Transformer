# 🎙️ Voice Changer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Built%20with-Python-blue.svg)](https://www.python.org/)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)

Transform your voice effortlessly! This Voice Changer application allows users to input an audio file and outputs the same content in a modified voice. Whether you want to sound like a robot, change your pitch, or apply fun effects, this project is the starting point for all your audio transformation needs.

---

## 🚀 Features

- **Audio Input**: Accepts audio files or real-time microphone input.
- **Voice Transformations**:
  - Pitch adjustment (high/low).
  - Robot voice effect.
  - Echo and reverb effects.
  - Custom transformations.
- **Real-Time Processing**: Transform and play back voice on-the-fly.
- **Multiple Format Support**: Works with common audio formats like `.wav`, `.mp3`, etc.

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or later
- `pip` package manager
- Basic audio hardware (microphone and speakers)

Ensure you have the necessary dependencies installed. Run:
```bash
pip install -r requirements.txt
```

## 🎛️ Usage Guide

Follow these steps to use the Voice Changer application:

### Using Pre-Recorded Audio Files

You can apply voice effects to existing audio files.

```
python main.py --file input/your-audio.wav --effect effect_name
```

The given effects which you can substitute in place of "effect_name" are robot , pitch_up , pitch_down , reverb

To Transform your voice as you speak using your microphone.

```
python main.py --realtime --effect effect_name
```
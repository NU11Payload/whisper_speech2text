# Speech-to-Text Application with Whisper

A Python application that provides speech-to-text functionality using OpenAI's Whisper model with an accessible and visually appealing user interface.

## Features

- **Speech Recording**: Record audio from your microphone
- **Speech-to-Text Transcription**: Convert speech to text using OpenAI's Whisper model
- **Accessible UI**: User-friendly interface with keyboard shortcuts
- **Text Management**: Copy, save, and clear transcribed text
- **Dark Mode**: Visually appealing dark theme

## Requirements

- Python 3.6+
- PyQt5
- PyAudio
- OpenAI Whisper
- NumPy
- SoundDevice
- SoundFile

## Installation

1. Ensure you have Python installed on your system
2. Activate the virtual environment:
   ```
   .\venv\Scripts\Activate.ps1  # On Windows PowerShell
   ```
3. The required packages should already be installed. If not, install them using:
   ```
   pip install openai-whisper pyqt5 pyaudio numpy sounddevice soundfile
   ```

## Usage

1. Activate the virtual environment (if not already activated):
   ```
   .\venv\Scripts\Activate.ps1  # On Windows PowerShell
   ```

2. Run the application:
   ```
   python main.py
   ```

3. Use the application:
   - Click "Record" or press F2 to start recording audio
   - Click "Stop" or press F2 again to stop recording
   - Click "Transcribe" or press F3 to transcribe the recorded audio
   - Click "Clear" or press F4 to clear the transcribed text
   - Click "Copy" or press F5 to copy the transcribed text to clipboard
   - Click "Save" or press F6 to save the transcribed text to a file

## Accessibility Features

- **Keyboard Shortcuts**: All functions can be accessed via keyboard shortcuts
- **High Contrast**: Dark theme with high contrast colors for better visibility
- **Clear Status Messages**: Status bar provides clear feedback on application state
- **Customizable Text Size**: Text area uses a readable font size

## How It Works

1. **Audio Recording**: The application uses PyAudio to record audio from your microphone and saves it as a WAV file.
2. **Speech Recognition**: OpenAI's Whisper model is used to transcribe the audio file to text.
3. **User Interface**: PyQt5 is used to create a visually appealing and accessible user interface.

## Troubleshooting

- **Audio Recording Issues**: Make sure your microphone is properly connected and selected as the default recording device in your system settings.
- **Transcription Quality**: For better transcription quality, speak clearly and minimize background noise.
- **Model Loading**: The first transcription might take some time as the Whisper model needs to be loaded.

## License

This project is open source and available under the MIT License.

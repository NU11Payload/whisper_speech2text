#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Speech-to-Text Application using OpenAI's Whisper

This application provides a user-friendly interface for transcribing speech to text
using OpenAI's Whisper model. It's designed with accessibility in mind and features
a visually appealing UI.
"""

import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, Qt
from ui import MainWindow
from audio_recorder import AudioRecorder
from whisper_transcriber import WhisperTranscriber

def main():
    """Main entry point of the application."""
    # Create the application
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Use Fusion style for a modern look
    
    # Create the main window
    window = MainWindow()
    
    # Create the audio recorder
    recorder = AudioRecorder()
    
    # Create the transcriber
    transcriber = WhisperTranscriber()
    
    # Connect signals and slots
    window.recordButton.clicked.connect(lambda: toggle_recording(window, recorder))
    window.transcribeButton.clicked.connect(lambda: transcribe_audio(window, recorder, transcriber))
    window.clearButton.clicked.connect(window.clear_text)
    window.copyButton.clicked.connect(window.copy_to_clipboard)
    window.saveButton.clicked.connect(window.save_to_file)
    
    # Show the window
    window.show()
    
    # Start the application event loop
    sys.exit(app.exec_())

def toggle_recording(window, recorder):
    """Toggle recording on/off."""
    if recorder.is_recording:
        recorder.stop_recording()
        window.set_recording_state(False)
    else:
        recorder.start_recording()
        window.set_recording_state(True)

def transcribe_audio(window, recorder, transcriber):
    """Transcribe the recorded audio."""
    if recorder.is_recording:
        recorder.stop_recording()
        window.set_recording_state(False)
    
    window.set_status("Transcribing...")
    
    # Get the audio file path
    audio_file = recorder.get_audio_file()
    
    if not os.path.exists(audio_file):
        window.set_status("No audio recorded yet.")
        return
    
    # Transcribe the audio
    text = transcriber.transcribe(audio_file)
    
    # Update the text area
    window.append_text(text)
    window.set_status("Transcription complete.")

if __name__ == "__main__":
    main()

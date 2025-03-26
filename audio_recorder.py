#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Audio Recorder Module

This module provides functionality for recording audio from the microphone
and saving it to a file for later transcription.
"""

import os
import tempfile
import wave
import numpy as np
import pyaudio
import threading

class AudioRecorder:
    """Class for recording audio from the microphone."""
    
    def __init__(self, sample_rate=16000, channels=1, chunk_size=1024):
        """Initialize the audio recorder.
        
        Args:
            sample_rate (int): The sample rate of the audio.
            channels (int): The number of audio channels.
            chunk_size (int): The size of audio chunks to process.
        """
        self.sample_rate = sample_rate
        self.channels = channels
        self.chunk_size = chunk_size
        self.format = pyaudio.paInt16
        self.is_recording = False
        self.frames = []
        self.pyaudio_instance = pyaudio.PyAudio()
        self.stream = None
        self.recording_thread = None
        
        # Create a temporary directory for storing audio files
        self.temp_dir = os.path.join(tempfile.gettempdir(), "whisper_stt")
        os.makedirs(self.temp_dir, exist_ok=True)
        
        # Set the audio file path
        self.audio_file = os.path.join(self.temp_dir, "recording.wav")
    
    def start_recording(self):
        """Start recording audio from the microphone."""
        if self.is_recording:
            return
        
        self.is_recording = True
        self.frames = []
        
        # Open the audio stream
        self.stream = self.pyaudio_instance.open(
            format=self.format,
            channels=self.channels,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size
        )
        
        # Start the recording thread
        self.recording_thread = threading.Thread(target=self._record)
        self.recording_thread.daemon = True
        self.recording_thread.start()
    
    def _record(self):
        """Record audio in a separate thread."""
        while self.is_recording:
            try:
                data = self.stream.read(self.chunk_size)
                self.frames.append(data)
            except Exception as e:
                print(f"Error recording audio: {e}")
                break
    
    def stop_recording(self):
        """Stop recording audio and save to file."""
        if not self.is_recording:
            return
        
        self.is_recording = False
        
        # Wait for the recording thread to finish
        if self.recording_thread and self.recording_thread.is_alive():
            self.recording_thread.join(timeout=1.0)
        
        # Close the audio stream
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
        
        # Save the recorded audio to a WAV file
        self._save_to_wav()
    
    def _save_to_wav(self):
        """Save the recorded audio to a WAV file."""
        if not self.frames:
            return
        
        with wave.open(self.audio_file, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.pyaudio_instance.get_sample_size(self.format))
            wf.setframerate(self.sample_rate)
            wf.writeframes(b''.join(self.frames))
    
    def get_audio_file(self):
        """Get the path to the recorded audio file.
        
        Returns:
            str: The path to the recorded audio file.
        """
        return self.audio_file
    
    def __del__(self):
        """Clean up resources."""
        if self.stream:
            self.stream.close()
        
        if self.pyaudio_instance:
            self.pyaudio_instance.terminate()

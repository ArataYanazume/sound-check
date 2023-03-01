#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyaudio
import wave

import struct
import numpy as np
import sounddevice as sd

import subprocess

def rec(
    channels = 1,
    chunk = 2**10,
    seconds = 5,
    samplerate = 44100,
    output_file = './output.wav'
    ):

    format = pyaudio.paInt16
    audio = pyaudio.PyAudio()
    info = pyaudio.PaMacCoreStreamInfo()

    # 音声設定
    stream = audio.open(
        format = format,
        channels = channels,
        rate = samplerate,
        input = True,
        input_device_index=0,
        frames_per_buffer = chunk,
        input_host_api_specific_stream_info=info
        )
    print('Recording ...')

    # 録音
    frames = []
    for _ in range(0, int(samplerate / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    print("Recording end")

    # 録音終了
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # 保存
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(format))
    wf.setframerate(samplerate)
    wf.writeframes(b''.join(frames))
    wf.close()


"""
Here's an example
of how you can record audio from your PC microphone
using the built-in wave module in Python without using PyAudio:

You can adjust the duration and sample rate to suit your needs.

This code uses the sounddevice package to record audio,
and the wave module to write the recorded audio to a wave file.
"""
def record_audio(filename="recording.wav", duration=5, fs=44100):
    # Start recording
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    # Write the recorded data to a wave file
    with wave.open(filename, "w") as wav_file:
        wav_file.setparams((1, 2, fs, 0, "NONE", "not compressed"))
        for sample in recording:
            wav_file.writeframes(struct.pack("<hh", *sample))


def record_mac_audio(filename="mac_audio.wav", duration=5):
    # Use the built-in "rec" command to record audio for the specified duration
    # subprocess.run(["rec", "-q", filename, "-c", "1", "-r", "44100", "-b", "16", "-t", "wav", "-d", str(duration)])
    cmd = [
        "rec",
        "-c",
        "1",
        "-r",
        "44100",
        filename,
        "trim",
        "0",
        str(duration)
    ]
    subprocess.run(cmd)

if __name__ == '__main__':
    rec()

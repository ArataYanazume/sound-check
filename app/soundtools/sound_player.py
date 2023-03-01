#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyaudio
import wave

# 音声再生
def play(
    chunk = 2**10,
    output_file = './output.wav'
    ):

    wf = wave.open(output_file, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
        )

    data = wf.readframes(chunk)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == '__main__':
    play()

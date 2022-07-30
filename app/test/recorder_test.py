#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyaudio
import wave

def rec(
    channels = 1,
    chunk = 2**10,
    seconds = 5,
    samplerate = 44100,
    output_file = "./output.wav"
    ):

    format = pyaudio.paInt16
    audio = pyaudio.PyAudio()

    # 音声設定
    stream = audio.open(
        format=format,
        channels=channels,
        rate=samplerate,
        input=True,
        frames_per_buffer=chunk
        )
    print("Recording ...")

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

if __name__ == '__main__':
    rec()
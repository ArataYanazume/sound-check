#!/usr/bin/env python
# -*- coding: utf-8 -*-
import soundtools as st

def rec_test(output_file='data/output.wav'):
    st.rec(output_file=output_file)

def system_test():
    import pyaudio
    soundObj = pyaudio.PyAudio()

    defaultCapability = soundObj.get_default_host_api_info()
    print(defaultCapability)

    isSupported = soundObj.is_format_supported(input_format=pyaudio.paInt16, input_channels=1, rate=48000, input_device=0)
    print(isSupported)

if __name__ == '__main__':
    rec_test(output_file='app/data/output.wav')

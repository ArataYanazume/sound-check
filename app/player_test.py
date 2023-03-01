#!/usr/bin/env python
# -*- coding: utf-8 -*-
import soundtools as st

def play_test(output_file='data/output.wav'):
    st.play(output_file=output_file)

if __name__ == '__main__':
    play_test(output_file='app/data/output.wav')

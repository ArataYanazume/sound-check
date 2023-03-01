# -*- coding: utf-8 -*-
import soundfile
from pydub import AudioSegment

EXPECTED_SAMPLE_RATE = 16000

# 音声変換
def convert_audio(user_file, output_file ='./converted.wav') -> bytes:

    # 音声ファイルを取り込む
    audio = AudioSegment.from_file(user_file)
    audio = audio.set_frame_rate(EXPECTED_SAMPLE_RATE).set_channels(1)
    audio.export(output_file, format='wav')

    output, _ = soundfile.read(output_file)
    return output.tobytes()

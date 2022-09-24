#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import logging
import grpc
import audio_pb2 as audio_pb2
import audio_pb2_grpc as audio_pb2_grpc
from utils import convert_audio

def run(fname, ports):
    audio = convert_audio(fname)
    channel = grpc.insecure_channel(ports)
    stub = audio_pb2_grpc.SimpleAudioStub(channel)
    response = stub.Recognize(audio_pb2.RecognizeRequest(audio=audio))
    print("Result: " + response.result)

if __name__ == '__main__':
    logging.basicConfig()

    args = sys.argv
    fname = args[1]
    ports = args[2]

    run(fname, ports)

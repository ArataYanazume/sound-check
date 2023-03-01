#!/usr/bin/env python
# -*- coding: utf-8 -*-
from concurrent import futures
import logging

import grpc
import audio_pb2 as audio_pb2
import audio_pb2_grpc as audio_pb2_grpc

# 音声認識
class SimpleAudio(audio_pb2_grpc.SimpleAudioServicer):
    def __init__(self):
        self.server_ok = 'Server OK'
        self.server_ng = 'Server NG'
    def Recognize(self, request, context):
        audio = request.audio
        if not audio:
            text = self.server_ng
        else:
            text = self.server_ok
        return audio_pb2.RecognizeResponse(result=text)

# gRPCサーバ起動
def serve_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    audio_pb2_grpc.add_SimpleAudioServicer_to_server(SimpleAudio(), server)
    server.add_insecure_port('[::]:20062')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()

    # gRPCサーバ起動
    serve_grpc()

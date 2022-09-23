#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
proto_src_root = os.path.normpath(os.path.join(ROOT_DIR, "proto/"))
proto_dst_root = os.path.normpath(os.path.join(ROOT_DIR, "."))
proto_fpath = os.path.normpath(os.path.join(ROOT_DIR, "proto", "audio.proto"))

cmd = [
    "python",
    "-m",
    "grpc_tools.protoc",
    "-I",
    f"{proto_src_root}",
    f"--python_out={proto_dst_root}",
    f"--grpc_python_out={proto_dst_root}",
    f"{proto_fpath}",
]

print(cmd)
subprocess.call(cmd)

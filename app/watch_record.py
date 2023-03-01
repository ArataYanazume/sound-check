#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import logging

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# 音声ファイル更新検知
def watch_audio():
    # 対象ディレクトリ
    DIR_WATCH = './app/data'
    # 対象ファイル名のパターン
    PATTERNS = ['*.wav']

    def on_modified(event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%s changed' % filename)

    event_handler = PatternMatchingEventHandler(PATTERNS)
    event_handler.on_modified = on_modified

    observer = Observer()
    observer.schedule(event_handler, DIR_WATCH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    logging.basicConfig()
    watch_audio()

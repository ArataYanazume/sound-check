# sound-check
Test program for various speech processing.


# ||PaMacCore (AUHAL)|| AUHAL component not found.||PaMacCore (AUHAL)|| OpenStream @ 48000 returned: -9999: Unanticipated host error
# ValueError: ('Unanticipated host error', -9999)
conda uninstall portaudio
pip uninstall pyaudio

brew install portaudio
pip install --global-option='build_ext' --global-option='-I/opt/homebrew/Cellar/portaudio/19.7.0/include' --global-option='-L/opt/homebrew/Cellar/portaudio/19.7.0/lib' pyaudio

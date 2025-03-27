import numpy as np
import sounddevice as sd


class AudioPlayer:
    def __init__(self, samplerate=24000, channels=1, dtype=np.int16):
        self.player = sd.OutputStream(samplerate=samplerate, channels=channels, dtype=dtype)
        self.player.start()

    def write(self, data):
        self.player.write(data)

    def close(self):
        if self.player:
            self.player.stop()
            self.player.close()

    def __del__(self):
        self.close()


def create_audio_buffer(duration_seconds=5, samplerate=24000):
    """Create an empty audio buffer of specified duration."""
    return np.zeros(samplerate * duration_seconds, dtype=np.int16)

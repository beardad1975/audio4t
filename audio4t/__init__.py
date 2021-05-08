from pydub import AudioSegment 
from pydub.generators import Sine , WhiteNoise, Square
from pydub.playback import play

from . import common

__all__ = [ 
            '正弦波', '播放聲音', '方波', '白噪音', 
            ]

# init
#common.speaker = win32com.client.Dispatch("SAPI.SpVoice")


# patch AudioSegment methods
# def 淡出(self, 持續時間):
#     return self.fade(to_gain=-120, duration=duration, end=float('inf'))

# def 淡入(self, 持續時間):
#     return self.fade(from_gain=-120, duration=duration, start=0)

AudioSegment.淡出 = AudioSegment.fade_out
AudioSegment.淡入 = AudioSegment.fade_in


class 正弦波(Sine):
    def __init__(self, 頻率, 取樣率=44100, 位元深度=16):
        Sine.__init__(self, 頻率, sample_rate=取樣率, bit_depth=位元深度)

    def 轉成聲音(self, 持續時間=1000.0, 音量=0.0):
        return self.to_audio_segment(duration=持續時間, volume=音量)

class 方波(Square):
    def __init__(self, 頻率, 取樣率=44100, 位元深度=16):
        Square.__init__(self, 頻率, sample_rate=取樣率, bit_depth=位元深度)

    def 轉成聲音(self, 持續時間=1000.0, 音量=0.0):
        return self.to_audio_segment(duration=持續時間, volume=音量)

class 白噪音(WhiteNoise):
    def __init__(self, 取樣率=44100, 位元深度=16):
        WhiteNoise.__init__(self, sample_rate=取樣率, bit_depth=位元深度)

    def 轉成聲音(self, 持續時間=1000.0, 音量=0.0):
        return self.to_audio_segment(duration=持續時間, volume=音量)


def 播放聲音(audio_segment):
    play(audio_segment)


if __name__ == '__main__' :
    pass
    

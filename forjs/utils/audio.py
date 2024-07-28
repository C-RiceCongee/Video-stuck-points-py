import time
import librosa
def GetAudioBeats(path):
   # 使用 librosa 加载音频
    y, sr = librosa.load(path)

    # 提取节拍信息
    tempo, beat_frames = librosa.beat.beat_track(y=2*y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    
    return beat_times
    
    
    
    
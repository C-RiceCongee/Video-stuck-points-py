import json
import os
import webview
import moviepy.editor as mpy
from forjs.utils.audio import GetAudioBeats
from forjs.utils.images import download_random_image, generate_random_image, resize_and_pad
def selectAudioFiles(window):
    def selectAudioFiles():
        file_types = ('Audio Files (*.wav;*.mp3;*.aac;*.flac)', 'All files (*.*)')
        result = window.create_file_dialog(
            webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types
        )
        path=result[0]
        img_dir = 'random_images'
        beat_times = GetAudioBeats(path)
        os.makedirs(img_dir, exist_ok=True)
        for i in range(len(beat_times)):
            api_url = "https://picsum.photos/200/300"  # 替换为实际的 API URL
            # 下载随机图片
            dir =  os.path.join(img_dir)
            filename =  f'image_{i}.png'
            fullFilePath =  os.path.join(os.path.join(dir), filename)
            if not fullFilePath:
                download_random_image(api_url, os.path.join(dir), filename)
            else:
                print(fullFilePath,'has exist !!')
        # 3. 创建视频剪辑
        clips = []
        for i in range(len(beat_times) - 1):
            start_time = beat_times[i]
            end_time = beat_times[i + 1]
            img_path = os.path.join(img_dir, f'image_{i}.png')
            # 填充白色改变像素～
            resize_and_pad(img_path,img_path,1080,2160)
            print(img_path)
            print(end_time,start_time)
            img_clip = mpy.ImageClip(img_path).set_duration(end_time - start_time)
            clips.append(img_clip)

        # 将音频文件添加到视频剪辑中
        final_video = mpy.concatenate_videoclips(clips).set_audio(mpy.AudioFileClip(path))

        # 保存最终视频
        # 打开文件夹选择对话框
        selected_directory = window.create_file_dialog(webview.FOLDER_DIALOG)

        # 输出选择的目录
        if selected_directory:
           final_video.write_videofile(selected_directory[0]+'/output.mp4', audio_codec='aac',fps=30)
        else:
            print("No directory selected.")
    return selectAudioFiles


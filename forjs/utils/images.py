import os
from urllib.parse import urlparse
import librosa
import moviepy.editor as mpy
from PIL import Image, ImageDraw
import random

import requests

# generate_random_image 本地生成图片
def generate_random_image(size=(640, 480)):
    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)
    for _ in range(10):  # 生成10个随机矩形
        x0, y0 = random.randint(0, size[0]), random.randint(0, size[1])
        x1, y1 = random.randint(0, size[0]), random.randint(0, size[1])
        if x0 > x1:
            x0, x1 = x1, x0
        if y0 > y1:
            y0, y1 = y1, y0
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.rectangle([x0, y0, x1, y1], fill=color)
    return image

# download_random_image 根据url随机下载图片
def download_random_image(url, target_directory,filename):
    # 发送 GET 请求获取图片
    response = requests.get(url)
    
    # 检查响应状态码
    if response.status_code == 200:
        # 解析 URL 获取文件名
        parsed_url = urlparse(url)
        # 构建完整的文件路径
        file_path = os.path.join(target_directory, filename)
        
        # 将图片数据写入文件
        with open(file_path, 'wb') as file:
            file.write(response.content)
        
        print(f"Image downloaded successfully: {filename}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")    
    


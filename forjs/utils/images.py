import json
import os
import time
from urllib.parse import urlparse
import librosa
import moviepy.editor as mpy
from PIL import Image, ImageDraw
import random
from datetime import date

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
async def download_random_image(url, target_directory,filename):
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
    

def resize_and_pad(image_path, output_path, width, height, background_color=(255, 255, 255)):
    # 打开图片
    img = Image.open(image_path)
    
    # 获取原始尺寸
    original_width, original_height = img.size
    
    # 计算宽高比
    aspect_ratio = original_width / float(original_height)
    
    # 根据宽高比计算新的尺寸
    if original_width >= original_height:
        new_width = width
        new_height = int(width / aspect_ratio)
    else:
        new_height = height
        new_width = int(height * aspect_ratio)
    
    # 调整图片尺寸
    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # 创建一个新的空白图片，颜色为白色
    new_img = Image.new("RGB", (width, height), background_color)
    
    # 计算粘贴的位置
    x_offset = (width - new_width) // 2
    y_offset = (height - new_height) // 2
    
    # 将调整后的图片粘贴到新图片上
    new_img.paste(resized_img, (x_offset, y_offset))
    
    # 保存图片
    new_img.save(output_path)
    


def download_500px_images(url_base):
    # 构建完整的 API URL
    url = f"{url_base}"
    
    # 发起 GET 请求
    response = requests.get(url)
    # 检查响应状态码
    if response.status_code == 200:
        # 解析 JSON 数据
        data = json.loads(response.text)
        # 提取图片 URL
        for item in data:
            image_url = item['url']['p4']
            
            # 构建图片名称
            image_name = image_url.split('/')[-1].split("!")[0]
            
            # 下载图片
            image_response = requests.get(image_url, stream=True)
            today = date.today().strftime("%Y-%m-%d")

            dirName = "500px_"+today
            os.makedirs(dirName, exist_ok=True)
            fullPath = os.path.join(dirName,image_name)
            if os.path.isfile(fullPath):
                print(f"has Downloaded: {image_name}")
                continue
            else:
                if image_response.status_code == 200:
                    # 保存图片到本地
                    with open(fullPath, 'wb') as file:
                        for chunk in image_response.iter_content(1024):
                            file.write(chunk)
                    print(f"Downloaded: {image_name}")
                else:
                    print(f"Failed to download: {image_url}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

import os
import sys
import webview

from forjs.lol import  selectAudioFiles
from forjs.utils.images import download_500px_images
def lol():
    print('LOL')
    return 'lol'


def expose(window):
    window.expose(lol,selectAudioFiles(window))  # expose functions beforehand

def resource_path(relative_path):
    """ Get absolute path to resource, works for both development and PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

html_path = resource_path('web/dist/index.html')
window = webview.create_window('Woah dude!', "web/dist/index.html")

url_base = "https://500px.com.cn/community/discover/rating?resourceType=0,2&category=&orderBy=rating&photographerType=&startTime=&page=1&size=100&type=json"
download_500px_images(url_base)
webview.start(expose, window,debug=True,http_server=True)

import os
import sys
import webview

from forjs.lol import  selectAudioFiles
def lol():
    print('LOL')
    return 'lol'

def wtf():
    print('WTF')

def echo(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

def expose(window):
    window.expose(lol, wtf,echo,selectAudioFiles(window))  # expose functions beforehand

def resource_path(relative_path):
    """ Get absolute path to resource, works for both development and PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

html_path = resource_path('web/dist/index.html')
window = webview.create_window('Woah dude!', "web/dist/index.html")

webview.start(expose, window,debug=True,http_server=True)
from moviepy.editor import VideoFileClip
import os

path = '/home/user/youtube-downloader-converter/music'

def convert_to_mp3(filename):
    clip = VideoFileClip(os.path.join(path,filename))
    clip.audio.write_audiofile(os.path.join(path,filename[:-4] + ".mp3"))
    clip.close()
import os

from pytube import YouTube


def download_video(url):
    yt = YouTube(url)
    filename = yt.filename.split(' - ')[1].split('Inside the NBA')[0].strip().replace(' ', '_')
    yt.set_filename(filename)
    video = yt.get('mp4', '720p')
    video.download(os.path.join(os.getcwd(), '/videos/'))
    return filename

import os

from pytube import YouTube


def download_video(url, on_finish):
    yt = YouTube(url)
    filename = yt.filename.split(' - ')[1].split('Inside the NBA')[0].strip().replace(' ', '_')
    yt.set_filename(filename)
    video = yt.get('mp4', '720p')
    print('Download {} started'.format(filename))
    video.download(os.path.join(os.getcwd(), '/videos/'), on_finish=on_finish)
    return filename

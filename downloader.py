from pytube import YouTube


def download_video(url):
    yt = YouTube(url)
    return yt.filename, yt.videos

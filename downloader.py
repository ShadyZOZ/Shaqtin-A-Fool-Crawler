from pytube import YouTube


def download_video(url):
    yt = YouTube(url)
    filename = yt.filename
    video = yt.get('mp4', '720p')
    video.download('/videos/')
    return filename

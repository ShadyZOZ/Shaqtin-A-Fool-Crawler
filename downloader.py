import os

import pafy


def download_video(url):
    print(url)
    video = pafy.new(url)
    best = video.getbest()
    filepath = best.download(os.path.join(os.getcwd(), 'videos'))
    return filepath

import os

import pafy


def download_video(url):
    video = pafy.new(url)
    best = video.getbest()
    best.download(os.path.join(os.getcwd(), 'videos'))
    return best.title

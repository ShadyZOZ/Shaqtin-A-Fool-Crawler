import os

import pafy


def download_video(url):
    print(url)
    video = pafy.new(url)
    best = video.getbest()
    filename = video.title.split(' - ')[1].split('Inside the NBA')[0].strip().replace(' ', '_') + '.' + best.extension
    filepath = best.download(os.path.join(os.getcwd(), 'videos', filename))
    return filepath

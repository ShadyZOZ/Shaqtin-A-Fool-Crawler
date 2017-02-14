import os

import pafy


def download_video(url):
    video = pafy.new(url)
    best = video.getbest()
    title = best.title.split(':')[1].split('|')[0].strip().replace(' ', '_')
    filename = '{0}.{1}'.format(title, best.extension)
    best.download(os.path.join(os.getcwd(), 'videos', filename))
    return filename

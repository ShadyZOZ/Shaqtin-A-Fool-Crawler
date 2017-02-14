from crawler import crawl
from db import VideoUrl
from downloader import download_video
from uploader import uploader


def download_url():
    for video_url in VideoUrl.objects(uploaded=False):
        key = download_video(video_url.url)
        uploader(key)
        video_url.uploaded = True
        video_url.name = key


def main():
    crawl()
    download_url()


if __name__ == '__main__':
    main()

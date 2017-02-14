from .crawler import crawl
from .db import VideoUrl
from .downloader import download_video


def download_url():
    for url in VideoUrl.objects(uploaded=False):
        print(download_video(url))


def main():
    crawl()
    download_url()


if __name__ == '__main__':
    main()

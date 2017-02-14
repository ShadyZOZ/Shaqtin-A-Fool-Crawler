from crawler import crawl
from db import VideoUrl
from downloader import download_video
from uploader import uploader


def download_url():
    for vdeo_url in VideoUrl.objects(uploaded=False):
        download_video(vdeo_url.url, uploader)


def main():
    crawl()
    download_url()


if __name__ == '__main__':
    main()

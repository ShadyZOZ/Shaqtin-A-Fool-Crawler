from crawler import crawl
from db import VideoUrl
from downloader import download_video


def download_url():
    for vdeo_url in VideoUrl.objects(uploaded=False):
        print(download_video(vdeo_url.url))


def main():
    crawl()
    download_url()


if __name__ == '__main__':
    main()

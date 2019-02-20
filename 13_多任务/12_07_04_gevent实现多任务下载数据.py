
from gevent import monkey
import gevent
import urllib.request


def downloader(imge_name, img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(imge_name, "wb") as f:
        f.write(img_content)


def main():

    gevent.joinall([
        gevent.spawn(downloader, '1.jpg',
                     'https://rpic.douyucdn.cn/live-cover/appCovers/2019/01/10/5447767_20190110032439_small.jpg'),
        gevent.spawn(downloader, '2.jpg',
                     'https://rpic.douyucdn.cn/live-cover/appCovers/2018/08/28/2165978_20180828195036_small.jpg'),
    ])


if __name__ == "__main__":
    main()

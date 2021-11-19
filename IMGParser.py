"""
На вход поступает файл html, в тегах которого содержатся ссылки <a> на изображения jpg/jpeg.
Скачивание происходит в директорию диска M "download_images"
"""
import requests, os, urllib.request, wget
from bs4 import BeautifulSoup as BS

count = 0
i = 0

while count != 82000:
    path ="D:/Downloads/Archive/messages/2000000015/messages" + str(count) + ".html"
    links = []

    file = open(path, "r")
    def parser(f):
        for line in f:
            if "=album" in line:
                links.append(line[36:].split("'")[0])
            else:
                pass
        file.close()
        download(i)

    def download(i):
        for link in links:
            wget.download(link, "M:/downloads_images/photo" + str(i) + ".jpg")
            i += 1

    parser(file)
    count += 50
    i += count

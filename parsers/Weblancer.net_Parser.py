from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


progects = []

def get_html(href):
    url = urlopen(href)
    soup = BeautifulSoup(url, 'html.parser')
    return soup

def parser(html):
    i = 0
    #progects = []
    while i <= 19:
        res = html.findAll('h2', class_='title')[i].text
        #print(res)
        theme = html.findAll('a', class_='text-muted')[i].text
        #print(theme)
        item = html.findAll('div', class_='col-sm-3 text-right text-nowrap hidden-xs')[i].text
        if item == 'нет заявок':
            progects.append({
                'Заказ: ':res,
                'Тема: ':theme,
                'Заявки':'0'
            })
        else:
            #print(item)
            progects.append({
                'Заказ: ':res,
                'Тема: ':theme,
                'Заявки':item[12]
            })
        
        i += 1
    #print(progects)

def main():
    number_page = 1
    path = 'https://www.weblancer.net/jobs/?page=' + str(number_page)
    while number_page <= 45:
        code = get_html(path)
        parser(code)
        number_page += 1
    file = open('prod.txt', 'w')
    for element in progects:
        file.write(str(element) + '\n')
    file.close()
        
if __name__ == '__main__':
    main()

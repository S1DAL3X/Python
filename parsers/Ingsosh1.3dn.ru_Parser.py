from bs4 import BeautifulSoup
from urllib.request import urlopen

file = open('schoolRes.txt', 'w')
output = []

def get_html(url):
    code_page = urlopen(url)
    soup = BeautifulSoup(code_page, 'html.parser')
    return soup

def parser(code):
    i = 0
    while i != 5:
        title = code.findAll('div', class_='eTitle')[i].text
        date = code.findAll('span', class_='e-date')[i].text
        view = code.findAll('span', class_='e-reads')[i].text
        
        output.append({
            'Заголовок': title,
            'Дата': date[5:],
            'Просмотров': view[11:]
        })
        
        i += 1
        
def parsePages():
    page = 1
    while page != 86:
        url = 'http://ingsosh1.3dn.ru/news/?page' + str(page)
        parser(get_html(url))
        page += 1
        
    for line in output:
        file.write(str(line) + '\n')
    file.write('Всего записей найдено: ' + str(len(output)))
        
def main():
    parsePages()

if __name__ == '__main__':
    main()
    
file.close()

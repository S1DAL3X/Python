#получим заголовки статей с первых 100 страниц clebfile.net и даты их публикации
from bs4 import BeautifulSoup
from urllib.request import urlopen

i = 0
href = 'http://clubfile.net/?q=node/288049&page=' + str(i)
output = []
dates = []
file = open('CLUBFILE.txt', 'w')

while i != 100:
    def get_html(href):
        url = urlopen(href)
        soup = BeautifulSoup(url, 'html.parser')
        return soup

    def parser(htmlCode):
        title = htmlCode.findAll('h2', class_='sifr-node-title')[1:]
        for line in title:
            article_title = line.find('a').text
            output.append(article_title)
        date = htmlCode.findAll('span', class_='submitted')
        for line in date:
            art_date = line.text
            dates.append(art_date)

        x = 0
        while x != len(output):
            for line in output:
                line = output[x] + ' \n' +  dates[x]
            file.write('\n' + '\n' + line + '\n' + '\n')
           #print(line + '\n')
            x += 1

    def main():
        parser(get_html(href))
        
    if __name__ == '__main__':
        main()
        
    i += 1
file.close()
print('ЗАПИСЬ ЗАВЕРШЕНА !!!')

#скрипт для шифровки\\дешифровки текста по принципу шифра Цезаря

alphavite = list(' abcdefghijklmnopqrstuvwxyz/\!?&,')#33
output = []

def coder(text, key):
    text = text.lower()       
    for label in text:
        position = alphavite.index(label)
        newPos = position + key
        while newPos > len(alphavite):
            newPos = newPos - len(alphavite)
        newLabel = alphavite[newPos]
        output.append(newLabel)
        
    for line in output:
        print(line, end='')
    
    
def decoder(text, key):
    text = text.lower()
    for label in text:
        position = alphavite.index(label)
        newPos = position - key
        newLabel = alphavite[newPos]
        output.append(newLabel)
    
    for line in output:
        print(line, end = '')
        
    
def main():
    choice = input('Вы хотите (З)акодировать или (Р)асшифровать текст? ')
    if choice == 'З':
        text = input('Введите текст: ')
        key = int(input('Введите ключ от 0 до 24: '))
        coder(text, key)
    elif choice == 'Р':
        text = input('Введите текст: ')
        key = int(input('Введите ключ: '))
        decoder(text, key)
    
main()
#Created by Aleksey Sidorenko

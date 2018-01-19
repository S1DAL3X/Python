#скрипт для шифрования и дешифровки текста алгоритмом ROT47
sub = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-=_+[]{}/?\!@#$%^&*()~,.:')
result = []

def rot47_coder(text):
    for label in text:
        position = sub.index(label)
        newPos = position + 13
        if newPos > len(sub):
            newPos = len(sub) - newPos
        for line in sub:
            if sub.index(line) == newPos:
                result.append(line)
            else:
                pass
    for letter in result:
        print(letter, end = '')
        
def rot47_decoder(text):
    for label in text:
        position = sub.index(label)
        newPos = position - 13
        if newPos > len(sub):
            newPos = newPos - len(sub)
        for line in sub:
            if sub.index(line) == newPos:
                result.append(line)
            else:
                pass
    for letter in result:
        print(letter, end = '')
        
def main():
    choice = input('Хотите (З)ашифровать или (Р)асшифровать текст ?  ')
    enter = input('Введите текст: ')
    if choice == 'З':
        rot47_coder(enter)
    elif choice == 'Р':
        rot47_decoder(enter)
    else:
        print('Ошибка ввода !')
    
main()

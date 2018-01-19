import hashlib

def decorator(function):
    def engine_encrypt():
        function()
        word = hashlib.md5(str(function).encode('utf-8'))
        print(word.digest())
        #print(word.hexdigest()) 
    return engine_encrypt

@decorator
def main():
    x = input('Input word: ')
    return x
    
main()
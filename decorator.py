#example of using decorator

def decorator(function):
    def wrapper():
        function(5, 7)
    return(wrapper)

@decorator
def funct(a, b):
    print(a + b)

funct()

# вариант 20
#задание 1 
g = (x for x in range(1 , 8))
print(list(g))


def announce(func):
    def wrapper():
        result = func()
        print('Сейчас вызов')
        return func() 
    return wrapper


@announce 
def hello():
    print('Привет!')


print(hello())

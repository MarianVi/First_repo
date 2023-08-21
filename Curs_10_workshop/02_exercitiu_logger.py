def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Data intrare args {args}')
        print(f'Data intrare kwargs {kwargs}')
        result = func(*args, **kwargs)
        print(f'Date iesire {result}')
        return result
    return wrapper

@logger
def suma(a, b):
    return a + b

@logger
def suma2(a, b, c):
    return a + b + c

suma(a = 3, b = 4)
suma(5, 6)
suma2(1, 2, c = 5)
suma2(7,8,9)
import readline

def read():
    return input('> ')

def eval(source):
    return source

if __name__ == '__main__':
    while True:
        print(eval(read()))

import platform

def main():
    message()

def message():
    version = platform.python_version()
    print(f'This is a python Version: {version}')
    print('Hello World!')
    print('Bye World')
    if True:
        print('True!')
    else:
        print('False!')


if __name__ == '__main__':
    main()
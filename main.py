import sys
from App import App


def main():
    try:
        app = App()
        app.on_execute()
    except:
        e = sys.exc_info()[0]
        print(f'Error: {e}')


if __name__ == '__main__':
    main()


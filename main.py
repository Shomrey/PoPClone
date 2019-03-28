from App import App


def main():
    try:
        app = App()
        app.on_execute()
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()


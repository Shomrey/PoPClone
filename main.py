from App import App
import traceback


def main():
    try:
        app = App()
        app.on_execute()
    except Exception as e:
        print(f'Error: {e}\n', traceback.format_exc())


if __name__ == '__main__':
    main()


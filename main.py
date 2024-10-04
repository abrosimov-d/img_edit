from actions import hello, helper
from actions.file import open, view, save, close
from actions.image import crop, rotate, scale, mirror, blur, sharp

def main():
    print('welcome to \"1 function = 1 action\" image editor!')
    app = {'actions':[]}
    _ = [module.register(app) for module in [helper, open, view, save, close, crop, rotate, scale, mirror, blur, sharp, hello]]
    _ = [print(f'input \'{action['hotkey']}\' for {action['name']}') for action in app['actions']]
    while True:
        select = input('input action (' + ''.join([action['hotkey'] for action in app['actions']]) + '): ')
        result = [action['function'](app) if select == action['hotkey'] else None for action in app['actions']]
        _ = [print(f'error: {error}') for error in result if error != None]

if __name__ == '__main__':
    main()
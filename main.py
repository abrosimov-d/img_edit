import filedialog, helper
from image import crop, rotate, scale, mirror, blur, sharp

def main():
    print('welcome to \"1 function = 1 action\" image editor!')
    app = {'actions':[]}
    _ = [module.register(app) for module in [filedialog, helper, crop, rotate, scale, mirror, blur, sharp]]
    _ = [print(f'input \'{action['hotkey']}\' for {action['name']}') for action in app['actions']]
    while True:
        select = input('input action (' + ''.join([action['hotkey'] for action in app['actions']]) + '): ')
        result = [action['function'](app) if select == action['hotkey'] else None for action in app['actions']]

if __name__ == '__main__':
    main()
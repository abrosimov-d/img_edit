from actions import about, helper
from actions.file import open, view, save
from actions.image import crop, rotate, scale, mirror, blur, sharp

def main():
    print('\nwelcome to \"1 function = 1 action\" image editor!')
    app = {'actions':[], 'changes': False}
    _ = [module.register(app) for module in [helper, open, view, save, crop, rotate, scale, mirror, blur, sharp, about]]
    _ = [print(f'input \'{action['hotkey']}\' for {action['name']}') for action in app['actions']]
    while True:
        try:
            select = input('input action (' + ''.join([action['hotkey'] for action in app['actions']]) + '): ')
            result = [action['function'](app) if select == action['hotkey'] else None for action in app['actions']]
            _ = [print(f'error: {error}') for error in result if error != None]
        except Exception as e:
            print('error:', e)

if __name__ == '__main__':
    main()
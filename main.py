import os

def open_file(app):
    print('open_file()')

def save_file(app):
    print('save_file()')

def close_file(app):
    print('close_file()')

def quit(app):
    print('good bye...')
    os._exit(0)

open_file_action = {
    'name': 'open file',
    'function': open_file,
    'hotkey': 'o'
}

save_file_action = {
    'name': 'save file',
    'function': save_file,
    'hotkey': 's'
}

close_file_action= {
    'name': 'close file',
    'function': close_file,
    'hotkey': 'c'
}

quit_action = {
    'name': 'quit program',
    'function': quit,
    'hotkey': 'q'
}

def debug(app):
    print(f'total {len(app['actions'])} actions')
    print(app['actions'])

debug_action = {
    'name': 'debug information',
    'function': debug,
    'hotkey': 'd'
}

def main():
    print('welcome to \"1 action = 1 function\" image editor!')
    app = {}
    app['actions'] = [open_file_action, save_file_action, close_file_action, quit_action, debug_action]

    while True:
        result = [print(f'input [{action['hotkey']}] for {action['name']}') for action in app['actions']]
        select = input()
        result = [action['function'](app) if select == action['hotkey'] else None for action in app['actions']]

if __name__ == '__main__':
    main()
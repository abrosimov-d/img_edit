import os, sys

def quit(app):
    if app['changes']:
        if app['yesno_action']['function']('save changes?'):
            app['save_action']['function'](app)
    print('good bye...')
    os._exit(0)

quit_action = {
    'name': 'quit program',
    'function': quit,
    'hotkey': 'q'
}

def debug(app):
    print(f'total {len(app['actions'])} actions')
    print(app)

debug_action = {
    'name': 'debug information',
    'function': debug,
    'hotkey': 'd'
}

def help(app):
    _ = [print(f'input \'{action['hotkey']}\' for {action['name']}') for action in app['actions']]

help_action = {
    'name': 'print this help',
    'function': help,
    'hotkey': 'h'
}

def register(app):
    app['actions'].append(quit_action)
    app['actions'].append(debug_action)
    app['actions'].append(help_action)
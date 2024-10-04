import os

# Exit application
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

# Print debug information
def debug(app):
    print(f'total {len(app['actions'])} actions')
    print(app['actions'])

debug_action = {
    'name': 'debug information',
    'function': debug,
    'hotkey': 'd'
}

# Print available actions
def help(app):
    _ = [print(f'input \'{action['hotkey']}\' for {action['name']}') for action in app['actions']]

help_action = {
    'name': 'print this help',
    'function': help,
    'hotkey': 'h'
}

# Register actions in application
def register(app):
    app['actions'].append(quit_action)
    app['actions'].append(debug_action)
    app['actions'].append(help_action)
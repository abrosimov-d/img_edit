def hello(app):
    print('hello world')

action = {
    'name': 'hello world',
    'function': hello,
    'hotkey': 'hw'
}

def register(app):
    app['actions'].append(action)
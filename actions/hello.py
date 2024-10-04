def hello(app):
    print('hello world')

action = {
    'name': 'hello world',
    'function': hello,
    'hotkey': 'w'
}

def register(app):
    app['actions'].append(action)
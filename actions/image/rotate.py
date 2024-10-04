def rotate_image(app):
    print('TODO: rotate image ')        

action = {
    'name': 'rotate image(s)',
    'function': rotate_image,
    'hotkey': '2'
}

def register(app):
    app['actions'].append(action)
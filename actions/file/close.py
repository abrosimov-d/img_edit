def close_file(app):
    for image in app['images']:
        print(image.shape)
    print('close_file()')

action= {
    'name': 'close file(s)',
    'function': close_file,
    'hotkey': 'c'
}

def register(app):
    app['actions'].append(action)

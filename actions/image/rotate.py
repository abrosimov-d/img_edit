def rotate_image(app):
    for filename in app['filenames']:
        print('TODO: rotate image ', filename)

action = {
    'name': 'rotate image',
    'function': rotate_image,
    'hotkey': '2'
}


def register(app):
    app['actions'].append(action)
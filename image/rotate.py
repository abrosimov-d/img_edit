def rotate_image(app):
    for filename in app['filenames']:
        print('TODO: rotate image ', filename)

rotate_image_action = {
    'name': 'rotate image',
    'function': rotate_image,
    'hotkey': '2'
}


def register(app):
    app['actions'].append(rotate_image_action)
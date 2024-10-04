def scale_image(app):
    for filename in app['filenames']:
        print('TODO: scale image ', filename)

action = {
    'name': 'scale image(s)',
    'function': scale_image,
    'hotkey': '3'
}


def register(app):
    app['actions'].append(action)
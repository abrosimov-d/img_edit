def scale_image(app):
    print('TODO: scale image ')

action = {
    'name': 'scale image(s)',
    'function': scale_image,
    'hotkey': '3'
}


def register(app):
    app['actions'].append(action)
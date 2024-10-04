def scale_image(app):
    for filename in app['filenames']:
        print('TODO: scale image ', filename)

scale_image_action = {
    'name': 'scale image',
    'function': scale_image,
    'hotkey': '3'
}


def register(app):
    app['actions'].append(scale_image_action)
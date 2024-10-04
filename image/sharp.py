def sharp_image(app):
    for filename in app['filenames']:
        print('TODO: sharp image ', filename)

sharp_image_action = {
    'name': 'sharp image',
    'function': sharp_image,
    'hotkey': '6'
}


def register(app):
    app['actions'].append(sharp_image_action)
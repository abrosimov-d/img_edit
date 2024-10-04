def blur_image(app):
    for filename in app['filenames']:
        print('TODO: blur image ', filename)

blur_image_action = {
    'name': 'blur image',
    'function': blur_image,
    'hotkey': '5'
}


def register(app):
    app['actions'].append(blur_image_action)
def mirror_image(app):
    for filename in app['filenames']:
        print('TODO: mirror image ', filename)

mirror_image_action = {
    'name': 'mirror image',
    'function': mirror_image,
    'hotkey': '4'
}


def register(app):
    app['actions'].append(mirror_image_action)
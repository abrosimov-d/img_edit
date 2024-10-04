def mirror_image(app):
    for filename in app['filenames']:
        print('TODO: mirror image ', filename)

action = {
    'name': 'mirror image(s)',
    'function': mirror_image,
    'hotkey': '4'
}


def register(app):
    app['actions'].append(action)
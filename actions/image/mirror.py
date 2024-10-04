def mirror_image(app):
    print('TODO: mirror image ')
    #return cv2.flip(image, 1)

action = {
    'name': 'mirror image(s)',
    'function': mirror_image,
    'hotkey': '4'
}


def register(app):
    app['actions'].append(action)
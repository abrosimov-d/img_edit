from cv2 import getRotationMatrix2D, warpAffine, rotate, ROTATE_90_CLOCKWISE, ROTATE_180, ROTATE_90_COUNTERCLOCKWISE

def rotate_image(app):
    error = None
    try:
        if 'images' not in app:
            app['open_action']['function'](app)

        side = input('input rotate side (0: 90-degree, 1: 180-degree, 2: 270-degree, empty: 90-degree): ')

        if side == '':
            side = 0
        else:
            side = int(side)

        app['images'] = [rotate(image, (ROTATE_90_CLOCKWISE, ROTATE_180, ROTATE_90_COUNTERCLOCKWISE)[side]) for image in app['images']]
        
        app['changes'] = True

    except Exception as e:
        error = e
    return error  

action = {
    'name': 'rotate image(s)',
    'function': rotate_image,
    'hotkey': '2'
}

def register(app):
    app['actions'].append(action)
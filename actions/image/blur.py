from cv2 import GaussianBlur

def blur_image(app):
    error = None
    try:
        if 'images' not in app:
            error = app['open_action']['function'](app)
            if error != None:
                return error


        radius = input('input gaussian blur radius (positive odd integer, empty for default 13): ')
        if radius == '':
            radius = 13
        else:
            radius = int(radius)

        if radius > 0 and radius % 2 == 1:
            app['images'] = [GaussianBlur(image, (radius, radius), 0) for image in app['images']]
            app['changes'] = True
        else:
            error = 'gaussian blur radius must be positive odd integer'
    
    except Exception as e:
        error = e
    return error

action = {
    'name': 'blur image(s)',
    'function': blur_image,
    'hotkey': '5'
}

def register(app):
    app['actions'].append(action)
from cv2 import flip

def mirror_image(app):

    error = None

    try:
        if 'images' not in app:
            error = app['open_action']['function'](app)
            if error != None:
                return error

        direction = input('input direction for clip (0 - vertical, 1 - horizontal), (empty - 0): ')

        if direction == '':
            direction = '0'

        if direction not in ('0', '1'):
            error = f'wrong input - {direction}'

        if error == None:
            app['images'] = [flip(image, int(direction)) for image in app['images']]
            app['changes'] = True

    except Exception as e:
        error = e

    return error    

action = {
    'name': 'mirror image(s)',
    'function': mirror_image,
    'hotkey': '4'
}

def register(app):
    app['actions'].append(action)
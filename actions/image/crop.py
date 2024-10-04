def crop_image(app):
    error = None
    try:
        if 'images' not in app:
            app['open_action']['function'](app)
        x, y, w, h = map(int, input('input x, y, width, height for crop: ').split(' '))
        app['images'] = [image[y: y + h, x: x + w] for image in app['images']]
        app['changes'] = True
    except Exception as e:
        error = e
    return error

action = {
    'name': 'crop image(s)',
    'function': crop_image,
    'hotkey': '1'
}

def register(app):
    app['actions'].append(action)
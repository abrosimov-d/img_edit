def crop_image(app):
    x, y, w, h = map(int, input('input x, y, width, height for crop: ').split(' '))
    app['images'] = [image[y: y + h, x: x + w] for image in app['images']]

crop_image_action = {
    'name': 'crop image',
    'function': crop_image,
    'hotkey': '1'
}

def register(app):
    app['actions'].append(crop_image_action)
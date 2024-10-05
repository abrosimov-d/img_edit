from cv2 import resize

def scale_image(app):
    error = None
    try:
        if 'images' not in app:
            app['open_action']['function'](app)

        value = input('input new size in px for long side (ex. 2000px) or scale factor in % (ex. 150%), (empty for 150%): ').replace(' ', '')
        if value == '':
            value = '150%'
        
        if value.find('px') > 0:
            print('px')
        elif value.find('%') > 0:
            print('%')
        else:
            error = f'wrong input: {value}'

        app['changes'] = True
    
    except Exception as e:
        error = e
    
    return error

    #return cv2.resize(image, None, fx=scale, fy=scale)

action = {
    'name': 'scale image(s)',
    'function': scale_image,
    'hotkey': '3'
}

def register(app):
    app['actions'].append(action)
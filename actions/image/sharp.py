from cv2 import filter2D, UMat, CV_32F
from numpy import array

def sharp_image(app):
    
    error = None
    
    try:
        if 'images' not in app:
            error = app['open_action']['function'](app)
            if error != None:
                return error

        kernel = array([[0, -1, 0], [-1, 5,-1],[0, -1, 0]])

        app['images'] = [filter2D(image, -1, kernel) for image in app['images']]

    except Exception as e:
        error = e
    
    return error

action = {
    'name': 'sharp image(s)',
    'function': sharp_image,
    'hotkey': '6'
}

def register(app):
    app['actions'].append(action)
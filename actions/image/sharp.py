from cv2 import filter2D, UMat

def sharp_image(app):
    print('TODO: sharp image')
    return
    kernel = [[0, -1, 0], 
              [-1, 5, -1], 
              [0, -1, 0]]
    app['images'] = [filter2D(image, -1, UMat(kernel)) for image in app['images']]

action = {
    'name': 'sharp image(s)',
    'function': sharp_image,
    'hotkey': '6'
}

def register(app):
    app['actions'].append(action)
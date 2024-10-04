from cv2 import imshow, waitKey, destroyAllWindows

def view_file(app):
    for image in app['images']:
        imshow('press any key for close window', image)
        waitKey(0)
    destroyAllWindows()

action = {
    'name': 'view file(s)',
    'function': view_file,
    'hotkey': 'v'
}

def register(app):
    app['actions'].append(action)

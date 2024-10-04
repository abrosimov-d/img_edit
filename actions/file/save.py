from os import listdir
from cv2 import imread, imshow, waitKey, destroyAllWindows

def save_file(app):
    if 'filenames' in app:
        for filename in app['filenames']:
            print(f'TODO: save {filename}')

action = {
    'name': 'save file',
    'function': save_file,
    'hotkey': 's'
}

def yesno(message):
    return 'y' == input(f'{message} \'y\' for yes, \'n\' for no: ')

yesno_action = {
    'name': 'yesno',
    'function': yesno,
    'hotkey': None
}


def register(app):
    app['actions'].append(action)
    app['save_action'] = action
    app['yesno_action'] = yesno_action
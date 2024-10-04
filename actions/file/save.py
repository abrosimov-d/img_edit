from os import listdir, path
from cv2 import imread, imshow, waitKey, destroyAllWindows, imwrite
from datetime import datetime

def short_file_name(filename):
    pass

def save_file(app):
    if not 'filenames' in app:
        app['open_action']['function'](app)
    directory = input('input directory for save file(s) (empty for .\\output): ')
    if directory == '':
        directory = '.\\output'
    savefilenames = input(f'input {len(app['filenames'])} file names separated space: (empty for add timestamp): ').split(' ')
    timestamp = datetime.now().strftime("%d.%m-%H.%M")
    if len(savefilenames) != len(app['filenames']):
        savefilenames = [f'{directory}\{path.basename(filename).replace('.', f'-{timestamp}.')}' for filename in app['filenames']]
    else:
        savefilenames = [f'{directory}\{filename}' for filename in savefilenames]
    for i in range(len(savefilenames)):
        print('save file to', savefilenames[i])
        imwrite(savefilenames[i], app['images'][i])
    app['changes'] = False

action = {
    'name': 'save file(s)',
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
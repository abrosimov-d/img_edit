from os import path, makedirs
from cv2 import imwrite
from datetime import datetime

def save_file(app):
    
    error = None

    try:

        if not 'images' in app:
            app['open_action']['function'](app)

        directory = input('input directory for save file(s) (empty for .\\output): ')
        if directory == '':
            directory = '.\\output'

        savefilenames = input(f'input {len(app['filenames'])} file names separated space: (empty for add timestamp): ').split(' ')
        timestamp = datetime.now().strftime("%d.%m-%H.%M")
        if len(savefilenames) != len(app['filenames']):
            savefilenames = [f'{directory}\\{path.basename(filename).replace('.', f'-{timestamp}.')}' for filename in app['filenames']]
        else:
            savefilenames = [f'{directory}\\{filename}' for filename in savefilenames]

        if not path.exists(directory):
            makedirs(directory)

        for i in range(len(savefilenames)):
            print('save file to', savefilenames[i])
            if False == imwrite(savefilenames[i], app['images'][i]):
                if error == None:
                    error = ''
                error += f'\nerror save file {savefilenames[i]}'
    
        app['changes'] = False
    
    except Exception as e:
        error = e

    return error

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
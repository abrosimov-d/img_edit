from os import listdir, path, sep
from cv2 import imread

def open_file(app):
    
    error = None
    
    try:
        directory = input(f'input directory for open file(s) (empty for .{sep}input): ')
        if directory == '':
            directory = f'.{sep}input'
            
        files = input('input file names separated space (empty for all files in directory): ')
        if files == '':
            files = listdir(directory)
        else:
            files = files.split(' ')
        
        if not 'filenames' in app:
            app['filenames'] = []

        for file in files:
            app['filenames'].append(f'{directory}{sep}{file}')

        if not 'images' in app:
            app['images'] = []
            for filename in app['filenames']:
                if path.isfile(filename):
                    image = imread(filename)
                    app['images'].append(image)
                    print(f'open file {filename} ({image.shape[0]}px x {image.shape[1]}px)')
                else:
                    if error == None:
                        error = ''
                    error += f'\nerror open file: {filename}'

    except Exception as e:
        error = e

    return error

action = {
    'name': 'open file(s)',
    'function': open_file,
    'hotkey': 'o'
}

def register(app):
    app['actions'].append(action)
    app['open_action'] = action

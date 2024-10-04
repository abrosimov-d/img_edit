from os import listdir
from cv2 import imread, imshow, waitKey, destroyAllWindows

def open_file(app):
    result = None
    try:
        directory = input('input directory for open file(s) (empty for .\\input): ')
        if directory == '':
            directory = '.\\input'
        files = input('input file names separated space (empty for all files in directory): ')
        if files == '':
            files = listdir(directory)
        else:
            files = files.split(' ')
        if not 'filenames' in app:
            app['filenames'] = []
            for file in files:
                app['filenames'].append(f'{directory}\\{file}')
        if not 'images' in app:
            app['images'] = []
            for filename in app['filenames']:
                print(f'open file {filename}')
                app['images'].append(imread(filename))
    except Exception as e:
        result = e
    return result

action = {
    'name': 'open file(s)',
    'function': open_file,
    'hotkey': 'o'
}

def register(app):
    app['actions'].append(action)
    app['open_action'] = action

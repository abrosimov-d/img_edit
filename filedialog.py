from datetime import datetime
from os import listdir
from cv2 import imread, imshow, waitKey, destroyAllWindows

def open_file(app):
    print('open_file()')
    directory = input('input directory (empty for ./input): ')
    if directory == '':
        directory = '.\input'
    files = input('input file names separeted space (empty for all files in directory): ')
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

open_file_action = {
    'name': 'open file',
    'function': open_file,
    'hotkey': 'o'
}


def view_file(app):
    for image in app['images']:
        imshow('image window', image)
        waitKey(0)
    destroyAllWindows()

view_file_action = {
    'name': 'view file',
    'function': view_file,
    'hotkey': 'v'
}


def save_file(app):
    print('save_file()')
    if 'filenames' in app:
        for filename in app['filenames']:
            print(f'save {filename}')

save_file_action = {
    'name': 'save file',
    'function': save_file,
    'hotkey': 's'
}


def close_file(app):
    for image in app['images']:
        print(image.shape)
    print('close_file()')

close_file_action= {
    'name': 'close file',
    'function': close_file,
    'hotkey': 'c'
}


def register(app):
    app['actions'].append(open_file_action)
    app['actions'].append(view_file_action)   
    app['actions'].append(save_file_action)
    app['actions'].append(close_file_action)
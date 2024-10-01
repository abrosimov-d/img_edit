from filedialog import open_file_dialog, save_file_dialog
from menu import menu

def tests():
    app = {'files': []}
    menu(app['files'])
    app['files'] = open_file_dialog()
    menu(app['files'])
    return    
    filenames = open_file_dialog()
    filenames = save_file_dialog(filenames)
    pass

if __name__ == '__main__':
    tests()
from filedialog import open_file_dialog, save_file_dialog

def tests():
    filenames = open_file_dialog()
    filenames = save_file_dialog(filenames)
    pass

if __name__ == '__main__':
    tests()
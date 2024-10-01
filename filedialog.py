def open_file_dialog():
    directory = input('enter directory: ')
    filenames = input('enter filename, or filenames separated space: ').split(' ')
    result = [f'{directory}\{filename}' for filename in filenames]        
    return result

def save_file_dialog(files):
    result = []
    return result
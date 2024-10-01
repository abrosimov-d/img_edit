from datetime import datetime

def open_file_dialog():
    directory = input('enter directory: ')
    filenames = input('enter filename, or filenames separated space: ').split(' ')
    result = [f'{directory}\{filename}' for filename in filenames]        
    return result

def save_file_dialog(filenames):
    result = []
    directory = input('enter directory: ')
    for filename in filenames:
        savefilename = input(f'enter filename for save {filename}:')
        timestamp = datetime.now().strftime("%d.%m-%H.%M")
        result.append(f'{directory}\{savefilename}-{timestamp}.png')
    return result
def about(app):
    print('''
\"1 function = 1 action\" image editor! - assignment for python course
date:\t08.10.2024
source:\thttps://github.com/abrosimov-d/img_edit
          ''')

action = {
    'name': 'about',
    'function': about,
    'hotkey': 'a'
}

def register(app):
    app['actions'].append(action)
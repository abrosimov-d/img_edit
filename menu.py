def menu(files):
    print('''main menu:
[o] - open file(s)
[s] - save file(s)
[c] - close file(s)
[a] - about
[q] - quit''')
    if len(files) > 0:
        print('''[1] - crop image
[2] - rotate image
[3] - scale image
[4] - miror image
[5] - blur image
[6] - sharp image
''')

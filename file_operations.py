def read_and_write(mode, name, text):
    if mode == 'w':
        with open(f'{name}.txt', mode=mode) as file:
            file.write(text)
    elif mode == 'r':
        with open(f'{name}.txt', mode=mode) as file:
            text_for_read = file.read()
        return text_for_read
    elif mode == 'a':
        with open(f'{name}.txt', mode=mode) as file:
            file.write(text)
    elif mode == 'a+':
        with open(f'{name}.txt', mode=mode) as file:
            file.write(text)
            file.seek(0)
            text_output = file.read()
        return text_output
    elif mode == 'w+':
        with open(f'{name}.txt', mode=mode) as file:
            file.write(text)
            file.seek(0)
            text_output = file.read()
        return text_output
    elif mode == 'r+':
        with open(f'{name}.txt', mode=mode) as file:
            print(file.read())
            file.seek(0)
            file.write(text)
            file.seek(0)
            text_output = file.read()
        return text_output

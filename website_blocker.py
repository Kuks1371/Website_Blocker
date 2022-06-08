import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com",
"www.twitter.com","twitter.com","www.youtube.com","youtube.com"]

def url_adder(n):
    for i in range(n):
        website_list.append(input("Enter url of website to block: "))

url_adder(int(input("Number of additional websites to block: ")))

starting_hour=int(input("Specify an hour to start blocking: "))
stoping_hour=int(input("Specify an hour to stop blocking: "))

while True:                                             
    if dt(dt.now().year,dt.now().month,dt.now().day,starting_hour) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,stoping_hour):                                       
        print("Blocking hours...")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Freedom hours...")
    time.sleep(5) #refresh rate for checking time

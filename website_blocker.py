import time
from datetime import datetime as dt

# Replace the websites_list with the websites you want to block
websites_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]

# Path to the hosts file on Windows (C:\Windows\System32\drivers\etc\hosts)
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# IP address to redirect the blocked websites to (localhost)
redirect_ip = "127.0.0.1"

def block_websites(start_hour, end_hour):
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, start_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_hour):
            with open(hosts_path, "r+") as file:
                content = file.read()
                for website in websites_list:
                    if website not in content:
                        file.write(redirect_ip + " " + website + "\n")
        else:
            with open(hosts_path, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websites_list):
                        file.write(line)
                file.truncate()
        time.sleep(5)

if __name__ == "__main__":
    # Set the start and end hours to block websites (24-hour format)
    start_hour = 9
    end_hour = 17

    block_websites(start_hour, end_hour)

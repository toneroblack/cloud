import os

url = ["google.com", "192.168.0.1", "192.168.0.12", "192.168.0.10", "192.168.0.14"]
for ip in url:
    reply = os.popen(f"ping {ip}").read()
    if "Received = 4" in reply:
        print(f"UP {ip}, The servers are up and running")
    else:
        print(f"DOWN {ip}, The servers are down. Contact your network administrator")

##SIMPLE PORT SCANNER
import socket
import pyfiglet
import sys
from scapy.all import *
from datetime import datetime
import json
import requests
import tkinter as tk

def url_check(url):
     try:
        socket.gethostbyname(url)
        return True
     except socket.error as e:
        print(f"Error occurred while checking URL {url}: {e}")
        return False
def geolocation(link):
     ip_addy = socket.gethostbyname(link)
     location = f"http://ipapi.co/{ip_addy}/json/"
     response = requests.get(location, timeout=10)
     data = response.json()
     print(f"Country: {data.get('country_name', 'N/A')}")
     print(f"Region: {data.get('region', 'N/A')}")
     print(f"City: {data.get('city', 'N/A')}")
     print(f"ISP: {data.get('org', 'N/A')}")
     print(f"Coordinates: {data.get('latitude', 'N/A')}, {data.get('longitude', 'N/A')}")
     print(f"Timezone: {data.get('timezone', 'N/A')}")

class txtwidget:
    def __init__(self, text_widget):
        self.text_widget = text_widget
    def write(self, string):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, string)
        if not string.endswith('\n'):
            string += '\n'
        self.text_widget.see(tk.END)
        self.text_widget.config(state=tk.DISABLED)
    def flush(self):
        pass

ports = Queue()
all_threads = []

def thread(host):
    while not ports.empty():
        port = ports.get()
        try:
            packet = IP(dst=host)/TCP(dport=port, flags="S")
            response = sr1(packet, timeout=0.5, verbose=0)
            if response:
                if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                    print(f"Port {port} is open", sep='\n')
                    sr(IP(dst=host)/TCP(dport=port, flags="R"), timeout=0.5, verbose=0)
                elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
                    pass
            else:
                pass
        except Exception as e:
            print(f"\nExiting program due to error: {e}")
            sys.exit(1)



def _scan():
    global scanning
    scanning = True
    host = input_box.get()
    if url_check(host):
        target = socket.gethostbyname(host)
    else:
        print("Invalid URL. Exiting...")
        sys.exit(1)

    print("-"*50)
    print("Scanning started at: " + str(datetime.now()))
    print("Scanning results for: " + str(target))
    geolocation(target)
    print("-"*50)
    try:
        iniport = int(port1.get())
        endport = int(port2.get())
        thread_count = int(thread_no.get())
        if iniport>=1 and endport<65536 and iniport<=endport:
            for port in range(iniport, endport + 1):
                ports.put(port)
            if thread_count:
                thread_count = int(thread_count)
            else:
                thread_count = 50
            for _ in range(thread_count):
                t = threading.Thread(target=thread, args=(target,))
                t.daemon = True
                t.start()
        else:
            print("Invalid port range. Please enter ports between 1 and 65535.")
    except ValueError:
        print("Invalid input. Please enter integers for ports and threads.")
    ports.join()
    print("Scanning finished at: " + str(datetime.now()))
    submit.config(state=tk.NORMAL)
            

def start_scan():
    submit.config(state=tk.DISABLED)
    thread = threading.Thread(target=_scan)
    thread.start()

def cancel_scan():
    global scanning
    if scanning:
        scanning = False
    else:
        print("Scanning cancelled by user.")

window = tk.Tk()
window.title("PortVision - Simple Port Scanner")
window.geometry("820x780")

main_frame = tk.Frame(window, padx=20, pady=20)
main_frame.pack()

label = tk.Label(main_frame, text=pyfiglet.figlet_format("PortVision"), font=("Courier", 7))
label.pack()

prompt_label = tk.Label(main_frame, text="Enter the host to scan:")
prompt_label.pack()

input_box = tk.Entry(main_frame, width=30)
input_box.pack(pady=5)

port1_label = tk.Label(main_frame, text="Enter the starting port (1-65535):")
port1_label.pack()

port1 = tk.Entry(main_frame, width=5)
port1.pack(pady=5)

port2_label = tk.Label(main_frame, text="Enter the ending port (1-65535):")
port2_label.pack()

port2 = tk.Entry(main_frame, width=5)
port2.pack(pady=5)

thread_label = tk.Label(main_frame, text="Enter number of threads to use (default 50):")
thread_label.pack()

thread_no = tk.Entry(main_frame, width=5)
thread_no.pack(pady=5)

submit = tk.Button(main_frame, text="Scan", command=start_scan)
submit.pack(pady=5)

cancel = tk.Button(main_frame, text="Exit", command=cancel_scan)
cancel.pack(pady=5)

output_box = tk.Text(main_frame, height=25, width=60)
output_box.pack(pady=5)

signature = tk.Label(main_frame, text="Created by ChrisY 2025", font=("Times New Roman", 8))
signature.pack(side=tk.BOTTOM)


sys.stdout = txtwidget(output_box)
sys.stderr = txtwidget(output_box)
window.mainloop()




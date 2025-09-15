# PortVision

## Why use a scanner like PortVision?
Let's say you just built a new website on your or someone's server. And now you want to check if ports are working in a secure way, that is, ports that ought to be opened are opened, and those who should be closed to prevent potential threats are closed according to whatever configuration you have set for them. This is the first step of consolidating the security of your newly-built website--making sure all the potential entry points of attackers, based on which are you able to further harden your server. Additionally. we do have the function of checking the geolocation of your server as well as the IPS that it's using, this might help with some specific security issue, too.

**Or**, you might be a new learner who just got into the field of network, and currently being curious on TCP/IP related stuff. PortVision is user friendly, for the fact that we have a simple user interface which allows users to type in whatever port range they want to scan, and how many threads they want to adopt during scanning. Not to mention the clear output may provide you with a more comprehensive understanding of what's going on during our process of connecting to another website.

And of course, after configuring a firewall (e.g., on a home router or cloud server), you can use PortVision from an external network to test if your rules are working correctly and consistently.

## Features
Host Verification: Automatically validates target URLs (just enter the url, both with the protocol name (https:// or http://) and without are okay)
**LEGAL WARNING: YOU ARE ONLY SCANNING THE WEBSITE AFTER GETTING PERMISSION FROM THE OWNER OF THE WEBSITE, OTHERWISE IT WOULD BE ILLEGAL**

SYN Scanning: Uses TCP SYN method for stealthier port detection, which means instead of performing a full TCP connection with the target, we only send a SYN packet to check if the handshake could be made, and then confirming the port status. This method provides us a more secure and efficient way of scanning

Geolocation: Displays target location and ISP information

Multi-threaded Scanning: Configurable thread count for efficient scanning

Real-time Results: Live output display during scanning

## Requirements
Python 3.x
Internet Connection during scanning
Scapy, pyfiglet, requests libraries installed

## Usage
### Run the program
`C:\Users\(YourHostName)\...\(TheFolderThatYouSavedTheScanner)\python PortVision.py`

### Enter information
<img width="1634" height="1612" alt="image" src="https://github.com/user-attachments/assets/45adec19-5bc2-448e-be6b-149d9d0d73d5" />
**Note that if you leave the thread number blank, it will go by default which is 50**

### And run it
<img width="954" height="534" alt="image" src="https://github.com/user-attachments/assets/a6d1a406-b53a-4499-b3d7-5f19483c3085" />







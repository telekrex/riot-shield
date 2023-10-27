<h1 align="center" style="margin-top: -10px"> Silencer </h1>
<p align="center" style="width: 100;">
   Instantly disable specific websites on a local machine, underneath all browsers.<br>
   Status: Complete<br>
   Supported platforms: Windows, Linux
</p>

## Pre-Requisites
- Python 3

## Installation & Setup
1. Clone or download this repository
2. For the script to work, you must enable read and write file permissions for the user that will use this, on the *hosts file* of the computer that will use this. Every OS has this file.  

 On Windows:  `C:\\Windows\\System32\\drivers\\etc\\hosts`  
 On Linux:  `/etc/hosts`  

#### What does this do?
The host file on your computer tells web browsers if they need to re-route to a specific IP address for a given domain name, and it's typically used to add aliases to locally networked devices. What Silencer does, is it uses Python to quickly and easily toggle the contents of that file between the default file and a custom file filled with new routes. This will not affect your web browsing for any websites you do not specify. The file titled `hosts default` is a copy of Microsoft's default host file. It is recommended to leave this file alone. For Linux users, this won't affect you as Linux's default host file is empty, or close to it, and both operating systems use the file the same way. The file titled `hosts silenced` is a list of websites you want to prevent this computer from reaching. The contents of that file in this repository are just examples.

## How to Use
Fill the contents of `hosts silenced` with a list of websites you wish to silence. Just make sure to keep the format, I'm not sure why you need to do it twice but that's how it works. Format:
>127.0.0.1 www.website.com  
>127.0.0.1 website.com  

`silencer.py` is responsible for turning the switch. Because all the program does is toggle the hosts list, the effects last until you switch it back. There's no background program or anything. There are multiple ways to do this.

#### Run the script manually (Linux)
In a terminal set to the directory where Silencer lives, run: `python3 silencer.py on` to turn on, `python3 silencer off` to turn off.

#### Run the script manually (Windows)
In a terminal set to the directory where Silencer lives, run: `python silencer.py on` to turn on, `python silencer off` to turn off.

#### Command Shortcut (Windows only)
Double click `silence.cmd` to turn on, `unsilence.cmd` to turn off.

## Credits
All code written by telekrex. Please report any security vulnerabilities to telekrex@gmail.com.

# Mute
Instantly toggle disabling of specific websites on a local machine, underneath all browsers.


## Getting Started
Requires: *Python 3*  
1. Install Python 3 if you don't have it
2. Download or clone this repository
3. You will need to enable read and write file permissions for the user that will use this, on the hosts file of the computer that will use this. Every computer has this file.  
    
 On Windows:  `C:\\Windows\\System32\\drivers\\etc\\hosts`  
 On Linux:  `/etc/hosts`  

## How to Use
The host file on your computer tells web browsers if they need to re-route to a specific IP address for a given domain name, and it's typically used to add aliases to locally networked devices. What Mute does, is it uses Python to quickly and easily toggle between the default file and a custom file filled with new routes. This will not affect your web browsing for any websites you do not specify.  

The file titled **hosts default** is a copy of Microsoft's default host file. It is recommended to leave this file alone. For Linux users, this won't affect you as Linux's default host file is empty, or close to it, and both operating systems use the file the same way.  

The file titled **hosts muted** is a list of websites you want to prevent this computer from reaching. By default the hosts muted file is just filled with some common distracting websites. On your computer, fill this file however you want. I'm not sure why, but you have to list it twice in the format:  
>127.0.0.1 www.website.com  
>127.0.0.1 website.com  

**mute.py** is responsible for turning the switch. You just turn it on or off, and the changes remain until you switch it again. There's no background program or anything.  

On Linux: Open a terminal and run: `python3 mute.py on` to turn on, `python3 mute.py off` to turn off.  
On Windows: Double click **mute.cmd** to turn on, **unmuted.cmd** to turn off, or use a terminal the same way as Linux.
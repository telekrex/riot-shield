<h1 align="center" style="margin-top: -10px"> Mute </h1>
<p align="center" style="width: 100;">
   toggle script that disables a custom list of hosts (urls) on a local machine.<br><br>
</p>

## Installation & Setup
0. Have a working Python 3
1. Clone or download this repository
2. Enable read and write file permissions for the user that will use this, on the *hosts file* of the computer that will use this. Every computer OS has this file.  

 On Windows:  `C:\\Windows\\System32\\drivers\\etc\\hosts`  
 On Linux:  `/etc/hosts`  

## What does this do?
The host file on your computer tells your computer if it needs to re-route to a specific IP address for a given domain name, and it's typically used to add aliases to locally networked devices. What `mute.py` does, is it uses Python to quickly and easily toggle the contents of that file between the default file and a custom file filled with aliases that you define (`targets.txt`), and in our case, re-routes any websites you list there to 127.0.0.1, so nowhere. This effectively blocks any feature of your OS from those websites, without messing around with browser extenstions or firewalls. This will not affect your web browsing for any websites you do not specify. The file titled `default.txt` is a copy of Microsoft's default host file. It is recommended to leave this file alone. For Linux users, this won't affect you as Linux's default host file is empty, or close to it, and both operating systems use the file the same way.

## How to Use
Fill the contents of `targets.txt` with a list of websites you wish to be able to mute. The contents of that file in this repository are just examples, but frankly, a decent list to start with.

Now, `mute.py` is responsible for turning the switch. Because all the program does is update the contents of the hosts file, the effects last until you switch it back. **There's no software running in the background.** There are multiple ways to run the script.

On Linux, any of these options should work:
- (terminal) `./enable.sh` to turn on, `./disable.sh` to turn off
- (terminal) `python3 mute.py enable` to turn on, `python3 mute.py disable` to turn off
- double-clicking `enable.sh` or `disable.sh`, after giving them executable permissions

On Windows, any of these options should work:
- double-clicking `enable.cmd` or `disable.cmd`
- (cmd) `enable` to turn on, `disable` to turn off
- (cmd) `python mute.py enable` to turn on, `python mute.py disable` to turn off

## Credits
Written by telekrex under GPL-3.0 license
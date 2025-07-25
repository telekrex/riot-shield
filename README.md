<h1 align="center" style="margin-top: -10px"> Riot Shield </h1>
<p align="center" style="width: 100;">
   <img src=".banner.jpg">
   Silence a custom list of hosts (URLs) on a local machine.
</p>
<p align="center">
   <a href="https://youtu.be/1l6vD7OHYVY">yum yum yum yum yum</a>
</p>

## Setup
1. Clone or download this repository
2. Enable read and write file permissions for the user that will use this, on the *hosts file* of the computer that will use this. Every computer OS has this file.  

 Location on Windows:  `C:\\Windows\\System32\\drivers\\etc\\hosts`  
 Location on Linux:  `/etc/hosts`  

## What does Riot Shield (`riot-shield.py`) do?
The host file on your computer tells your computer if it needs to re-route to a specific IP address for a given domain name, and it's typically used to add aliases to locally networked devices. What `riot-shield.py` does, is it uses Python to quickly and easily toggle the contents of that file between the default file and a custom file filled with aliases that you define (`targets.txt`), and in our case, re-routes any websites you list there to 127.0.0.1, so nowhere. This effectively blocks any feature of your OS from those websites, without messing around with browser extenstions or firewalls. This will not affect your web browsing for any websites you do not specify. The file titled `default.txt` is a copy of Microsoft's default host file. It is recommended to leave this file alone. For Linux users, this won't affect you as Linux's default host file is empty, or close to it, and both operating systems use the file the same way.

## How to Use
Fill the contents of `targets.txt` with a list of websites you wish to be able to block. The contents of that file in this repository are just examples, but frankly, a decent list to start with.

Now, `riot-shield.py` is responsible for turning the switch. Because all the program does is update the contents of the hosts file, the effects last until you switch it back. **There's no software running in the background.** There are multiple ways to run the script.

Run `python riot-shield.py enable` to turn on, `python riot-sheild.py disable` to turn off. (`python3` on some Linux machines).

I personally recommend creating cmd or shell scripts to run these commands, and I've included examples in the repository.

## Credits
Written by telekrex.

## License
This project is released into the public domain. See the [LICENSE](LICENSE) file for details.
# mute
Disable (or re-enable) a selection of distracting URLs on your local machine with one click.
<br /br>
Double-click **mute.cmd** to turn on/enable. It will run **mute.py** with the `on` argument, and this will copy the contents of **hosts muted** to your computer's hosts file. What this does if you follow the 127.0.0.1 pattern provided from the repo (intended as a sample), is re-route any of the URLs on the right to the IP on the left. This works underneath any browser features, on all browsers. To customize, enter your own contents into the hosts muted file. Since this tool works by modifying a file, there's no program that needs to be running. It is simply on until turned off.
<br /br>
Double-click **unmuted.cmd** to turn off/disable. This will do a similar thing to turning on, but instead uses **hosts default**, which is a file that contains the defaults you want. The sample in this repo contains the same content you will find on modern Windows computers, and it's recommended that you not really change this file. Only change it if you want something very specific to be in your defaults.
<br /br>
This should work on Windows and Linux automatically, unless your hosts file is located somewhere other than the standard location. If so, just modify **mute.py**.

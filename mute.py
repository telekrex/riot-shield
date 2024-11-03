#!/usr/bin/env python3
# Written by telekrex
# under GPL-3.0 license

import sys
from platform import system

# read what platform is running,
# and use that to set HOSTS constant,
# which = the path of the "hosts" file;
if system() == 'Windows':
    # on Windows, the path is this:
    HOSTS = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
else:
    # on Linux, it's this:
    HOSTS = '/etc/hosts'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

try:
    # (sys.argv[1] should be a string added to the input of
    # running mute.py; example: "mute.py enable")
    # if the provided arg is one of several words that mean
    # to "enable" the muting (feel free to add more),
    if str(sys.argv[1]).lower() in ['enable', 'start', 'on']:
        # open the HOSTS file as writable,
        with open(HOSTS, 'w') as hostsfile:
            # open 'targets.txt' as readable,
            with open('targets.txt', 'r') as targetsfile:
                # and begin to build contents
                # to write to the HOSTS file
                assembly = ''
                # by reading each line and making it
                # into a host alias directing to home
                for line in targetsfile.read().split('\n'):
                    assembly += f'127.0.0.1 {line}\n127.0.0.1 www.{line}\n'
                # when done assembling,
                # write to file.
                hostsfile.write(assembly)
        # finally, let the user know
        # everything went ok...
        print('Hosts muted. Job done.')
        # program will then exit.

    else:
        # if anything other than "enable" was asked for in arg,
        # then we assume "disable" and write HOSTS file to the
        # contents of 'default.txt', which should be our backup.
        # open the HOSTS file as writable,
        with open(HOSTS, 'w') as hostsfile:
            # open 'default.txt' as readable,
            with open('default.txt', 'r') as defaultfile:
                contents = defaultfile.read()
                hostsfile.write(contents)
        # finally, let the user know
        # everything went ok...
        print('Hosts returned to default. Job done.')
        # program will then exit.

except Exception as e:
    # if something went wrong, show the user,
    print(e)
    # and might as well point user to a place to report.
    print('\nPlease forward any issues to telerex@gmail.com')
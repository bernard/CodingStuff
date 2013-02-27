#!/usr/bin/python

# This programs run a shell cmd which is "ps auxww"
# then print the result if PID > 200 and cmd begins with "/"

import subprocess
import re

p = subprocess.Popen(['ps auxww'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

regex = re.compile('^/')

for line in p.stdout.readlines():
    a = line.split()
    if a[1] == "PID":
	print line,
    else:
        if int(a[1]) > 200:
            if regex.match(a[10]):
                print line,


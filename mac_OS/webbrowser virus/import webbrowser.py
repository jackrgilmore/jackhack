#!/usr/bin/env python

#functionality for self-deletion
from os import remove
from sys import argv

import webbrowser as wb
name="HACKED!"
extension=".txt"

for i in range (5):
    wb.open("https://jackrgilmore.github.io/jackhack/")
    file = open("Desktop/"+ str(0+i+1) + name + extension, "w")
    file.write("YOU'VE BEEN HACKED!")

remove[argv(0)]

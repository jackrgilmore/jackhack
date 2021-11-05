#!/usr/bin/env python
import os
import webbrowser as wb
name="hack"
extension=".txt"

for i in range (5):
    wb.open("https://jackrgilmore.github.io/jackhack/")
    file = open("Desktop/"+ name + str(i+1) + extension, "w")
    file.write("YOU'VE BEEN HACKED!")
    file.close()

os.remove[os.argv(0)]
#!/usr/bin/env python3

import os
from os import remove
from sys import argv
from os.path import expanduser
from os.path import join
extension = str(".txt")
name = ("spam")

for i in range(100):
    file = open(name + str(i+1) + extension, "w")
    file.write("YOU'VE BEEN HACKED!")
    file.close()

#comment out deleting self
#remove(argv[0])

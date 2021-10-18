<<<<<<< HEAD
#!/usr/bin/env python
=======
#!/usr/bin/env python3
>>>>>>> main

import os
from os import remove
from sys import argv
from os.path import expanduser
from os.path import join
extension = str(".txt")
name = ("spam")

for i in range(100):
<<<<<<< HEAD
    file = open("Desktop/"+ name + str(i+1) + extension, "w")
=======
    file = open("Desktop/" + name + str(i+1) + extension, "w")
>>>>>>> main
    file.write("YOU'VE BEEN HACKED!")
    file.close()

#comment out deleting self
<<<<<<< HEAD
remove(argv[0])
=======
#remove(argv[0])
>>>>>>> main

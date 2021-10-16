from os import remove
from sys import argv
extension = str(".txt")

for i in range(100):
    create = open("spam" + str(i + 1) + extension, "w+")
    create.write("YOU'VE BEEN HACKED!")
    create.close()

remove(argv[0])

import re

file = open("testfile.txt", "r")
listips = open("listips.txt", "w")

x = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", file)

listips.write(x)

file.close()
listips.close()
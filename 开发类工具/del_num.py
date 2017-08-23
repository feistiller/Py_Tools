# File: readline-example-1.py
import time
file1 = open("input.txt")
lines = file1.readlines()
file1.close()
file2 = open(r'output.txt', 'w')
for line in lines:
    if not line:
        print ('over')
        break
    else:
        line = line[3:]
        time.sleep(0.3)
        print line
        file2.write(line)
    pass

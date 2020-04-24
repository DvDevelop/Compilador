import time
import sys

print(sys.argv)
if(len(sys.argv)>1):
    print("pass")
    print(sys.argv[1])
else:
    print("no pasas")
time.sleep(5)

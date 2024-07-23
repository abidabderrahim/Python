import time
import sys

take_time = int(input("Enter the time in seconds: "))
for x in range(take_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60)
    hours = int(x / 3600)
    sys.stdout.write('\r' + f"{hours:02}:{minutes:02}:{seconds:02}")
    sys.stdout.flush()
    time.sleep(1)
sys.stdout.write('\r')
sys.stdout.flush()

print("TIME's UP!")

import datetime
import time
import os

def get_current_time():
    return datetime.datetime.now().replace(microsecond=0)

start_time = get_current_time()

try:
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("job started at:", start_time.time())
        print("hit Ctrl + C to stop working")

        elapsed = get_current_time() - start_time
        print("working for:", elapsed)
except KeyboardInterrupt:
    end_time = get_current_time()
    elapsed = end_time - start_time
    print("time elapsed:", elapsed)

# in future
# saving to file
# calculate whole project work time
# specify what project want to work with
# add flag to specify a path

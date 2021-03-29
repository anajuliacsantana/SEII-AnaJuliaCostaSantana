import threading
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...\n')

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    
finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds(s)')
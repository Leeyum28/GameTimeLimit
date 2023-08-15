from datetime import datetime
from time import time
import subprocess

def block_game():
    current_time_day = datetime.now()
    current_time =  int(float(current_time_day.strftime('%H:%M:%S')))
    end_time = current_time + str(4000)

    while current_time() < end_time:
        time_left = int(end_time - time.time())
        print(time_left / 60)
        
    print("\nTime limit reached")
    subprocess.call(['taskkill', '/F', '/IM', 'steam.//rungameid1938090'])

if __name__ == '__main__':
    block_game()    
block_game()
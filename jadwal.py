from datetime import datetime
import time
import os
while True:
    #print(datetime.now().second)
    if datetime.now().hour==21:
        os.system('python3 upload.py')
        time.sleep(3600)
    else:
        time.sleep(3600)
        continue

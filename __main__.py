from datetime import datetime
import time
from raspi_auto_grow import *

# Check interval time
CHECK_INTERVAL_IN_SECONDS = 20

while(True):
    if soil_is_dry():
        print(datetime.now(),
              'Soil seems to be dry, watering the plant now.')
        notify.send(str(datetime.now().strftime(
            "%d.%m.%Y, %H:%M:%S")) + ' > Watering :)')
        run_pump()
    else:
        print(datetime.now(),
              'Soil seems to be humid, won\'t water the plant.')
    time.sleep(CHECK_INTERVAL_IN_SECONDS)

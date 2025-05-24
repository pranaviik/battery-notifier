import time
import psutil 
from plyer import notification 

notified= False
last_reminder= 0

while True:
    battery= psutil.sensors_battery()
    percent= battery.percent
    plugged= battery.power_plugged
    
    if(percent==100 and plugged):
        current_time=time.time()
        
        if(not notified):
            notification.notify(
                title="Battery fully charged",
                message="Battery is at 100%. PLease unplug the charger",
                timeout=10
            )
            notified=True
            last_reminder= current_time
        elif current_time-last_reminder>=900:
            notification.notify(
                title="REMINDER",
                message=("Still plugged in. Please unplug."),
                timeout=10
            )
            last_reminder= current_time
    elif not plugged:
        notified= False
        exit()
    
    time.sleep(60)

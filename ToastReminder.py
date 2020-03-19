
import time
import datetime

#run    "pip install win10toast"     if not done already
from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast("Timing Reminders","This is how you will be reminded")

data = []
for d in open("times").read().split():
    if len(d.split("~")) == 3:
        data.append(d.split("~"))

while True:
    if datetime.datetime.today().weekday() < 5: # is a weekday (mon=0, sun=6)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        for t in data:
            if current_time == t[0]:  #if the time is the same, then show the notification
                toaster.show_toast(
                    t[1],
                    t[2],
                    icon_path=None,
                    duration=60,
                    threaded=True
                    )
                time.sleep(70) # will mean that it never notifies more than needed (it may notify many times within the minute otherwise)
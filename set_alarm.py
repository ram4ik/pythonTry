import sched
import time

def set_alarm(alarm_time, message):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time, 1, print, argument=(message,))
    print('Alarm set for', time.asctime(time.localtime(alarm_time)))
    s.run()

set_alarm(time.time()+3, 'Wake up!')
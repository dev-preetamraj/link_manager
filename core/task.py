from celery import shared_task
from time import sleep
from .models import MeetLink
from datetime import date, datetime
import calendar

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def show_live_meeting(user):
    day = calendar.day_name[date.today().weekday()]
    meets = MeetLink.objects.filter(user = user,day=day)
    live_meet = []
    for meet in meets:
        current_time = datetime.now().time()
        start_time = meet.start_time
        end_time = meet.end_time
        if current_time>=start_time and current_time<=end_time:
            live_meet.append(meet)
    return live_meet


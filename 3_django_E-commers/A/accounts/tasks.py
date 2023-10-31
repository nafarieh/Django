from celery import shared_task
from accounts.models import OtpCode
from datetime import datetime, timedelta
import pytz

#Doc
#https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html

#Github celery
#https://github.com/celery/django-celery-beat

#supervisor commands.txt
#https://github.com/amirbigg/oneFile-codes/blob/master/supervisor_commands.txt

@shared_task
def remove_expired_otp_codes():
    expired_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
    OtpCode.objects.filter(created__lt=expired_time).delete()







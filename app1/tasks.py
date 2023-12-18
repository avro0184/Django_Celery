from time import sleep
from celery import shared_task


@shared_task
def test_func():
    sleep(2)
    print("Hi>>>>>>>>>>>>>>>>..")
    



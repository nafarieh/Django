from django.test import TestCase
from bucket import bucket
from celery import shared_task

# Create your tests here.



# TODO: can be async?
def all_bucket_objects_task():
	result = bucket.get_objects()
	return result

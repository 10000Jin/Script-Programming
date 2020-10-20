import random
import time
import os


# ------------------------- mpPool -------------------------

def my_func(work):
    print("일(={0})에 Process ID = {1}".format(work, os.getpid()))
    time.sleep(1)
    return work




# ------------------------- mpProcess -------------------------

def seconds_timer(end_time):
	start_time = time.time()
	while True:
		time.sleep(0.001)
		if time.time() - start_time >= end_time:
			break
	proc = os.getpid()
	print("{0} seconds have elapsed by process id: {1}". format(end_time, proc))




# ------------------------- mpQueue -------------------------


def data_creator(max_data_number, q):
	print("creating data!")
	for _ in range(max_data_number):
		data = random.random()
		q.put(data)
	q.put(None)

def data_consumer(q):
	while True:
		data = q.get()
		if data is None:
			break
		print("consuming data is {}", format(data))
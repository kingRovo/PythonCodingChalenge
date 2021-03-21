import time

def jobscheduler(f, n):
	time.sleep(n/1000)
	return f()

print(time.ctime())
print(jobscheduler(lambda: "Hi! " + time.ctime(), 2000))

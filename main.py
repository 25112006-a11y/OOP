import time
t=time.localtime()
time_string=time.strftime("%m/%d/%Y, %H:%M:%S",t)
print(time_string)
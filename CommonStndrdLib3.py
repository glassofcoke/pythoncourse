import time

#Get the current timestamp
time_now = time.time()
print("Time stamp: ", time_now)

#Get the local time
localtime = time.localtime(time_now)
print("Local time: ", localtime)

#Converts in a more readable string
localtime = time.asctime(localtime)
print("Local time: ", localtime)

#We can specify the format of the time string will look like
print("Local Time: ", time.strftime("%Y-%m-%d %H:%M:%S",time.localtime() ))
import thread,time

def a():
   while True:
      time.sleep(0.01)
      print("aa ")

def b():
   while True:
      time.sleep(0.02)
      print("bb ")

try:
   thread.start_new_thread(a, ())
   thread.start_new_thread(b, ())
except:
   print "Error: unable to start thread"

while 1:
   pass

import threading
import time


class LockedThread(threading.Thread):
    def __init__(self, name, increment):
        threading.Thread.__init__(self) #calling parent class initialization method
        self.name = name
        self.increment = increment

    def run(self):
        print("Playing game \n")
        LockingThread.acquire() #locking thread
        countdown(self.name, 1, self.increment) #delay of 1 seconds
        LockingThread.release() #unlocking thread
        print("End game\n")

class Threads(threading.Thread):
    def __init__(self, name, increment):
        threading.Thread.__init__(self)
        self.name = name
        self.increment = increment

    def run(self):
        print("Commencing " + self.name + "\n")
        LockingThread.acquire()
        LockingThread.release()
        countdown(self.name, 1, self.increment)
        print("Exiting: " + self.name + "\n")


def countdown(name, delay, increment):
    for i in range(1, increment+1):
        x = i
        time.sleep(delay)
        print (f"{x}s until {name} stops executing \n")


LockingThread = threading.Lock()

item1 = LockedThread("Play game", 5)
item2 = Threads("XP increase", 5)
item3 = Threads("Congratulations page", 2)


item1.start()
item2.start()
item3.start()
item1.join()
item2.join()
item3.join() 
print("End of execution") #join() methods makes sure this line gets executed last 

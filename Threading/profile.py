import time 
import threading

def get_name(names):
    for name in names:
        time.sleep(0.2)
        print('names:' + name)

def get_house_name(house_names):
    for house_name in house_names:
        time.sleep(0.2)
        print('house_name: ' + house_name)

name = ['max', 'kevin', 'alex']
house_name =['slytherin', 'gryffindor', 'hermiones']
car_name = []
thread1 = threading.Thread(target = get_name, args =(name,))
thread2 = threading.Thread(target =get_house_name, args =(house_name,))
thread1.start()
thread2.start()

thread1.join()
thread2.join()

        
import time
import threading

def calc_square_area(numbers):
    print('calculate the square of numbers')
    for n in numbers:
        time.sleep(0.2)
        print('square:', n*n)
        
def calc_cube(numbers):
    print('calculate the cube of numbers')
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n*n*n) 

arr = [2, 4, 5, 8, 9]
t = time.time()
t1 = threading.Thread(target = calc_square_area, args =(arr,))
t2 = threading.Thread(target = calc_cube, args =(arr,))

t1.start()
t2.start()

t1.join()
t2.join()
print ('Done in :',time.time() -t)
print('Hah! I am done with all my work')